"""
Figure generation script for:
"A Unified Predictive Coding Account of Functional Self-Awareness in Bees"

Generates all 4 figures as high-resolution PDFs for paper inclusion.
Requires: numpy, matplotlib
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import json
import os

np.random.seed(2026)
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

# ---- shared style ----
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -15, 15)))

def meta_accuracy_analytical(precision, slope=4.0):
    u = 1.0 - precision
    p_out_hard = sigmoid(u * slope - 1.0)
    p_out_easy = sigmoid(u * slope - 2.5)
    return (p_out_hard + (1 - p_out_easy)) / 2


# ============================================================
# FIGURE 1 — Precision-Metacognition Inverted-U
# ============================================================
print("Generating Fig 1: Precision-Metacognition Inverted-U...")

fig, ax = plt.subplots(figsize=(6.5, 4.0))

precision_grid = np.linspace(0.01, 0.99, 999)

# Main curve (slope=4.0)
meta_main = np.array([meta_accuracy_analytical(p, slope=4.0) for p in precision_grid])
ax.plot(precision_grid, meta_main, color='#2171b5', lw=2.5, label='Slope = 4.0 (main)')

# Robustness band: slopes 2.0 to 6.0
slopes = np.linspace(2.0, 6.0, 20)
meta_band = np.array([[meta_accuracy_analytical(p, slope=s) for p in precision_grid] for s in slopes])
ax.fill_between(precision_grid, meta_band.min(axis=0), meta_band.max(axis=0),
                alpha=0.2, color='#2171b5', label='Slope range [2.0, 6.0]')

# Find and annotate optimum
opt_idx = np.argmax(meta_main)
opt_p = precision_grid[opt_idx]
opt_acc = meta_main[opt_idx]
ax.axvline(opt_p, color='#e34a33', lw=1.5, linestyle='--', alpha=0.8)
ax.annotate(
    f'p* = {opt_p:.2f}\nacc* = {opt_acc:.3f}',
    xy=(opt_p, opt_acc), xytext=(opt_p + 0.10, opt_acc - 0.012),
    fontsize=10, color='#e34a33',
    arrowprops=dict(arrowstyle='->', color='#e34a33', lw=1.2)
)

# Shade regions
ax.axvspan(0.01, 0.35, alpha=0.06, color='#fc8d59', label='Low precision\n(opts out on everything)')
ax.axvspan(0.78, 0.99, alpha=0.06, color='#91bfdb', label='High precision\n(overconfident, never opts out)')

ax.set_xlabel('Precision (p)', fontsize=12)
ax.set_ylabel('Metacognitive accuracy', fontsize=12)
ax.set_title('Precision-Metacognition Trade-off: Inverted-U Relationship', fontsize=12)
ax.set_xlim(0, 1)
ax.set_ylim(0.55, 0.70)
ax.legend(loc='lower center', ncol=2, fontsize=9, framealpha=0.7)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "fig1_inverted_u.pdf"))
fig.savefig(os.path.join(OUT_DIR, "fig1_inverted_u.png"))
plt.close()
print("  -> fig1_inverted_u.pdf")


# ============================================================
# FIGURE 2 — GCA Factor Across Conditions
# ============================================================
print("Generating Fig 2: GCA Factor Across Conditions...")

with open(os.path.join(os.path.dirname(__file__), "..", "simulation_results_r2.json")) as f:
    res = json.load(f)

conditions = ['normal', 'disrupted', 'nurse_spatial', 'forager_spatial']
labels = ['Normal', 'Disrupted', 'Nurse\n(spatial)', 'Forager\n(spatial)']
gca_pcts = [res[c]['gca_factor_pct'] * 100 for c in conditions]
precisions = [res[c]['precision'] for c in conditions]

colors_bar = ['#2171b5', '#e34a33', '#31a354', '#756bb1']

fig, ax1 = plt.subplots(figsize=(7.0, 4.0))

x = np.arange(len(conditions))
bars = ax1.bar(x, gca_pcts, color=colors_bar, alpha=0.85, width=0.55, edgecolor='white', lw=1.5)

for bar, val in zip(bars, gca_pcts):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_ylabel('GCA factor (% variance explained)', fontsize=12)
ax1.set_ylim(0, 100)
ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontsize=11)
ax1.axhline(50, color='gray', lw=1.0, linestyle=':', alpha=0.6)
ax1.set_title('General Cognitive Ability Factor Across Conditions', fontsize=12)

# Secondary axis: precision
ax2 = ax1.twinx()
ax2.plot(x, precisions, 'ko--', ms=7, lw=1.8, label='Mean precision', zorder=5)
ax2.set_ylabel('Mean precision', fontsize=12)
ax2.set_ylim(0, 1.0)
ax2.spines['top'].set_visible(False)

lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines2, labels2, loc='upper right', fontsize=10)

plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "fig2_gca_factor.pdf"))
fig.savefig(os.path.join(OUT_DIR, "fig2_gca_factor.png"))
plt.close()
print("  -> fig2_gca_factor.pdf")


# ============================================================
# FIGURE 3 — Cross-Domain Correlation Matrix (Normal)
# ============================================================
print("Generating Fig 3: Correlation Matrix...")

# Regenerate individual-level data to get full correlation matrix
N = 500
precisions_norm = np.random.beta(5, 2, N) * 0.75 + 0.2  # normal condition

def meta_accuracy_analytical_vec(prec, slope=4.0):
    u = 1.0 - prec
    p_out_hard = sigmoid(u * slope - 1.0)
    p_out_easy = sigmoid(u * slope - 2.5)
    return (p_out_hard + (1 - p_out_easy)) / 2

meta_v = meta_accuracy_analytical_vec(precisions_norm)
caste = 0.5
tool_v = np.clip(precisions_norm * (0.5 + 0.5 * caste) + np.random.normal(0, 0.05, N), 0, 1)
learning_v = np.clip(0.5 + 0.45 * precisions_norm * caste + np.random.normal(0, 0.03, N), 0, 1)
gca_v = np.clip(0.5 + 0.4 * precisions_norm + np.random.normal(0, 0.04, N), 0, 1)

data = np.vstack([meta_v, tool_v, learning_v, gca_v])
corr = np.corrcoef(data)
domain_labels = ['Meta-\ncognition', 'Tool\nUse', 'Caste\nLearning', 'GCA\nScore']

fig, ax = plt.subplots(figsize=(5.5, 4.5))
im = ax.imshow(corr, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
cbar = plt.colorbar(im, ax=ax, shrink=0.85)
cbar.set_label("Pearson's r", fontsize=11)

ax.set_xticks(range(4))
ax.set_yticks(range(4))
ax.set_xticklabels(domain_labels, fontsize=10)
ax.set_yticklabels(domain_labels, fontsize=10)
ax.set_title('Cross-Domain Correlation Matrix\n(Normal Condition, N=500)', fontsize=11)

for i in range(4):
    for j in range(4):
        val = corr[i, j]
        color = 'white' if abs(val) > 0.5 else 'black'
        weight = 'bold' if (i == 0 and j == 3) or (i == 3 and j == 0) else 'normal'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                fontsize=10, color=color, fontweight=weight)

# Box the key anti-correlation cells
for (i, j) in [(0, 3), (3, 0)]:
    ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, fill=False,
                                edgecolor='black', lw=2.5))

ax.annotate('Key anti-\ncorrelation', xy=(3, 0), xytext=(3.6, -0.4),
            fontsize=9, color='#e34a33',
            arrowprops=dict(arrowstyle='->', color='#e34a33', lw=1.2))

plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "fig3_corr_matrix.pdf"))
fig.savefig(os.path.join(OUT_DIR, "fig3_corr_matrix.png"))
plt.close()
print("  -> fig3_corr_matrix.pdf")


# ============================================================
# FIGURE 4 — Disruption Effects and Meta-GCA Sign Flip
# ============================================================
print("Generating Fig 4: Disruption Effects and Sign Flip...")

fig = plt.figure(figsize=(10.0, 4.2))
gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.35)

# --- Left panel: Domain scores normal vs disrupted ---
ax_left = fig.add_subplot(gs[0])
domains = ['Meta-\ncognition', 'Tool\nUse', 'Caste\nLearning']
normal_vals = [res['normal']['meta'], res['normal']['tool'], res['normal']['learning']]
disrupted_vals = [res['disrupted']['meta'], res['disrupted']['tool'], res['disrupted']['learning']]

x = np.arange(len(domains))
width = 0.35
b1 = ax_left.bar(x - width/2, normal_vals, width, label='Normal', color='#2171b5', alpha=0.85)
b2 = ax_left.bar(x + width/2, disrupted_vals, width, label='Disrupted', color='#e34a33', alpha=0.85)

for bar in b1:
    ax_left.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                 f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)
for bar in b2:
    ax_left.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                 f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=9)

ax_left.set_xticks(x)
ax_left.set_xticklabels(domains, fontsize=10)
ax_left.set_ylabel('Mean accuracy', fontsize=12)
ax_left.set_ylim(0, 0.85)
ax_left.set_title('Domain Scores: Normal vs. Disrupted', fontsize=11)
ax_left.legend(fontsize=10)
ax_left.grid(axis='y', alpha=0.3)

# --- Right panel: Meta-GCA correlation across conditions ---
ax_right = fig.add_subplot(gs[1])
meta_gca_vals = [res[c]['corr_meta_gca'] for c in conditions]
bar_colors = ['#2171b5' if v < 0 else '#e34a33' for v in meta_gca_vals]

bars = ax_right.bar(range(len(conditions)), meta_gca_vals, color=bar_colors, alpha=0.85,
                    edgecolor='white', lw=1.5, width=0.55)
ax_right.axhline(0, color='black', lw=1.0, linestyle='-')

for bar, val in zip(bars, meta_gca_vals):
    ypos = bar.get_height() + 0.02 if val >= 0 else bar.get_height() - 0.06
    ax_right.text(bar.get_x() + bar.get_width()/2, ypos,
                  f'r={val:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax_right.set_xticks(range(len(conditions)))
ax_right.set_xticklabels(labels, fontsize=10)
ax_right.set_ylabel("Meta-GCA Pearson's r", fontsize=12)
ax_right.set_ylim(-1.0, 1.0)
ax_right.set_title('Metacognition-GCA Correlation\n(Sign Flip Under Disruption)', fontsize=11)
ax_right.grid(axis='y', alpha=0.3)

# Annotate sign flip
ax_right.annotate('',
    xy=(1, meta_gca_vals[1] - 0.03), xytext=(0, meta_gca_vals[0] + 0.03),
    arrowprops=dict(arrowstyle='->', color='black', lw=1.5, connectionstyle='arc3,rad=-0.2'))
ax_right.text(0.65, 0.0, 'Sign\nflip', fontsize=9, ha='center', style='italic')

plt.suptitle('Effects of Circadian Disruption on Domain Performance and Cross-Domain Coupling',
             fontsize=11, y=1.02)

fig.savefig(os.path.join(OUT_DIR, "fig4_disruption.pdf"), bbox_inches='tight')
fig.savefig(os.path.join(OUT_DIR, "fig4_disruption.png"), bbox_inches='tight')
plt.close()
print("  -> fig4_disruption.pdf")

print("\nAll figures generated in:", OUT_DIR)
print("Files:")
for f in sorted(os.listdir(OUT_DIR)):
    print(" ", f)
