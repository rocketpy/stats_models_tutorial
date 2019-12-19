import pstats
import cProfile as profile
from profile_fibonacci_memoized import fib, fib_seq


# create 5 set of stats
for i in range(5):
    filename = 'profile_stats_{}.stats'.format(i)
    profile.run('print({}, fib_seq(20))'.format(i), filename)

# read all 5 stats files into a single object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_{}.stats'.format(i))

# clean up filenames for the report
stats.strip_dirs()

# sort the statistics by the cumulative time spent in the function
stats.sort_stats('cumulative')

stats.print_stats()
