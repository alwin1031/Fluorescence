import pandas as pd
import matplotlib.pyplot as plt


def Baseline(df):
    shf = sum(df["Data"][0:10]) / 10
    df["Data"] = [(x - shf) for x in df["Data"]]
    shf2 = sum(df["Data"][60:70]) / 10
    df["Data"] = [((x - shf2)/shf2)*100 for x in df["Data"]]
    return df


def Figure(df):
    fig, ax = plt.subplots(dpi=300)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(width=1.5)
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(1.5)
    font1 = {'family': 'arial', 'color':  'black', 'weight': 'bold', 'size': 12}
    font2 = {'family': 'arial', 'color':  'black', 'weight': 'bold', 'size': 15}
    plt.plot(df.s, df.Data, c="black", lw=1)
    plt.axis([60, 150, -10, 100])   # [xmin, xmax, ymin, ymax]
    plt.xlabel("Time (s)", fontdict=font1, labelpad=8)
    plt.ylabel("RFC (% initial)", fontdict=font1, labelpad=10)
    plt.title(title, fontdict=font2, pad=10)


if __name__ == '__main__':
    import sys
    import os
    input_path = sys.argv[1]
    title = sys.argv[2]
    df = pd.read_excel(input_path, skiprows=33)
    input_path = os.path.splitext(input_path)[0]

    df = Baseline(df)
    Figure(df)

    plt.savefig(input_path+".png")
    print('Done! d(//-v-)b')
