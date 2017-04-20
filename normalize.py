import csv
from tabulate import tabulate

def collect_data(state_populations, gt_populations):
    states = [row['*State or territory*'] for row in state_populations.values()]
    stats = []
    for state in states:
        # Skip states that were on Wikipedia but not in the GT data.
        if state not in gt_populations.keys():
            next

        stats.append({
            'name': state,
            'gt_pop': int(gt_populations[state]['U_Total'].replace(',', '')),
            'us_pop': int(state_populations[state]['Population estimate, July 1, 2016'].replace(',', ''))
        })
    gt_total = sum([state['gt_pop'] for state in stats])
    us_total = sum([state['us_pop'] for state in stats])
    for state in stats:
        state['gt_percent'] = state['gt_pop'] / gt_total
        state['us_percent'] = state['us_pop'] / us_total
    return stats

def main():
    with open('state_pops.csv') as f:
        state_csv = csv.DictReader(f)
        state_populations = {row['*State or territory*']: row for row in state_csv}

    with open('gt_pops.csv') as f:
        gt_csv = csv.DictReader(f)
        gt_populations = {row['State']: row for row in gt_csv}

    stats = collect_data(state_populations, gt_populations)
    # Convert `stats` to a list of lists so we can print it as a table.
    table_stats = [[s['name'], s['gt_pop'], s['us_pop'], s['gt_percent'], s['us_percent'], int((s['gt_percent'] - s['us_percent']) * 100)] for s in stats]

    # Sort the table so overrepresented states (i.e. Georgia) are on top.
    table_stats = sorted(table_stats, key=lambda k: k[-1], reverse=True)

    # Add a '%' to everything in the 'Difference' column.
    for s in table_stats:
        s[-1] = str(s[-1]) + '%'

    print(tabulate(table_stats, headers=['State', 'GT Pop', 'US Pop', 'GT Percent', 'US Percent', 'Difference']))

if __name__ == '__main__':
    main()
