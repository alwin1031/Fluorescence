import pandas as pd
import matplotlib.pyplot as plt

def pre_read(pre_df):
    for i in range(len(pre_df.iloc[:,0])):
        if pre_df.iloc[i,0] == 'Data Points':
            skip_line = i+2
            break
    return skip_line


def Baseline(df):
    shf = sum(df["Data"][0:10]) / 10
    df["Data"] = [(x - shf) for x in df["Data"]]
    shf2 = sum(df["Data"][60:70]) / 10
    df["Data"] = [((x - shf2)/shf2)*100 for x in df["Data"]]
    df["s"] = [(x - 60) for x in df["s"]]
    return df


def Figure(df):
    fig, ax = plt.subplots(dpi=300, figsize=(8,6))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(width=1.8)
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(1.8)
    font1 = {'family': 'arial', 'color':  'black', 'weight': 'bold', 'size': 18}
    font2 = {'family': 'arial', 'color':  'black', 'weight': 'bold', 'size': 26}
    plt.plot(df.s, df.Data, c="black", lw=1.2)
    plt.axis([0, 90, -10, 100])   # [xmin, xmax, ymin, ymax]
    plt.xlabel("Time (s)", fontdict=font1, labelpad=10)
    plt.ylabel("RFC (% initial)", fontdict=font1, labelpad=10)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.subplots_adjust(bottom=0.14)
    plt.title(title, fontdict=font2, pad=20)


if __name__ == '__main__':
    import sys
    import os
    input_path = sys.argv[1]
    title = sys.argv[2]
    # Pre-read the excel to find where data start from
    pre_df = pd.read_excel(input_path)
    skip_line = pre_read(pre_df)
    # Import data
    df = pd.read_excel(input_path, skiprows=skip_line)
    input_path = os.path.splitext(input_path)[0]

    df = Baseline(df)
    Figure(df)

    plt.savefig(input_path+".png")
    print('Done! d(//-v-)b')
