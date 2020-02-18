from scipy.stats import mannwhitneyu

t = [95.76,
95.92,
95.08,
94.56,
95.58,
96.61,
93.9,
94.9,
92.36,
96.1]
g = [86.83,
98.50,
97.83,
97.83,
98.50,
97.83,
97.00,
99.00,
99.00,
100.00]
mannwhitneyu(t,g)

stat, p = mannwhitneyu(t, g)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
print(p)
if p > alpha:
	print('Same distribution (fail to reject H0)')
else:
	print('Different distribution (reject H0)')