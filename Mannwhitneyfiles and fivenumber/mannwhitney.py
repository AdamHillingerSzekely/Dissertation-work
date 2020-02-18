from scipy.stats import mannwhitneyu

t = [95.077]
g = [99.95]
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