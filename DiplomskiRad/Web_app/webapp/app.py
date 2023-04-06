#streamlit run app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

air_ns = pd.read_csv("pin_cop_ns_air_web - Copy.csv", index_col = [0])
rain_ns = pd.read_csv("pin_cop_ns_rain_web - Copy.csv", index_col = [0])
soil_ns = pd.read_csv("pin_cop_ns_soil_web - Copy.csv", index_col = [0])
temp_ns = pd.read_csv("pin_cop_ns_temp_web - Copy.csv", index_col = [0])

air_os = pd.read_csv("pin_cop_os_air_web - Copy.csv", index_col = [0])
rain_os = pd.read_csv("pin_cop_os_rain_web - Copy.csv", index_col = [0])
wind_os = pd.read_csv("pin_cop_os_wind_web - Copy.csv", index_col = [0])
temp_os = pd.read_csv("pin_cop_os_temp_web - Copy.csv", index_col = [0])



st.set_page_config(
     page_title='Data Analysis',
     initial_sidebar_state="expanded",
)
params = {"ytick.color" : "w",
          "xtick.color" : "w",
          "axes.labelcolor" : "w",
          "axes.edgecolor" : "w",
          "axes.titlecolor" : "w",
          "text.color" : "w",
          "axes.facecolor" : "#00172B",
          "axes.labelsize":36}
plt.rcParams.update(params)
sns.set(rc={'axes.facecolor':'#00172B',
            'figure.facecolor':'#00172B',
            "ytick.color": "w",
            "xtick.color": "w",
            "axes.labelcolor": "w",
            "axes.edgecolor": "w",
            "axes.titlecolor": "w",
            "text.color": "w",
            "axes.labelsize": 36
            })


sideb = st.sidebar
check1 = sideb.button("Check or not?")
check2 = sideb.button("Wind")
check3 = sideb.button("Temperature")
check4 = sideb.button("Soil")
check5 = sideb.button("Air conditions")
check6 = sideb.button("Rain")



if check1:
    iris = sns.load_dataset('iris')
    st.title('Iris Dataset Scatterplot')
    st.write(
        'The iris dataset is a classic dataset in machine learning and statistics. It contains measurements of the physical characteristics of three different species of iris flowers: setosa, versicolor, and virginica.')
    fig, ax = plt.subplots()
    ax = sns.scatterplot(data=iris, x='sepal_length', y='petal_length', hue='species')
    st.pyplot(fig)


elif check2:
    st.title('Wind')
    st.write('This is the second page of the app.')

elif check3:

    option = st.selectbox(
        "Location",
        ("Osijek", "Novi Rok"))

    st.title('Temperature')

    if (option == "Novi Rok"):

        fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
        fig.suptitle('Temperature comparisons and correlation')

        sns.heatmap(temp_ns.corr(method='pearson'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[0])
        axes[0].set_title("Pearson")

        sns.heatmap(temp_ns.corr(method='kendall'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[1])
        axes[1].set_title("Kendall")

        sns.heatmap(temp_ns.corr(method='spearman'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[2])
        axes[2].set_title("Spearman")

        fig.patch.set_facecolor("#00172B")

        st.pyplot(fig)

        st.pyplot(sns.pairplot(data=temp_ns, height=10, aspect=1))

    elif(option == "Osijek"):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
        fig.suptitle('Temperature comparisons and correlation')

        sns.heatmap(temp_os.corr(method='pearson'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[0])
        axes[0].set_title("Pearson")

        sns.heatmap(temp_os.corr(method='kendall'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[1])
        axes[1].set_title("Kendall")

        sns.heatmap(temp_os.corr(method='spearman'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[2])
        axes[2].set_title("Spearman")

        fig.patch.set_facecolor("#00172B")

        st.pyplot(fig)

        st.pyplot(sns.pairplot(data=temp_os, height=10, aspect=1))



elif check4:
    st.title('Soil')
    st.write('This is the second page of the app.')

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    fig.suptitle('Soil comparisons and correlation')

    sns.heatmap(soil_ns.corr(method='pearson'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[0])
    axes[0].set_title("Pearson")

    sns.heatmap(soil_ns.corr(method='kendall'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[1])
    axes[1].set_title("Kendall")

    sns.heatmap(soil_ns.corr(method='spearman'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[2])
    axes[2].set_title("Spearman")

    fig.patch.set_facecolor("#00172B")

    st.pyplot(fig)

    st.pyplot(sns.pairplot(data=soil_ns, height=10, aspect=1))

elif check5:
    st.title('Air conditions')
    st.write('This is the second page of the app.')

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    fig.suptitle('Air conditions comparisons and correlation')

    sns.heatmap(air_ns.corr(method='pearson'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[0])
    axes[0].set_title("Pearson")

    sns.heatmap(air_ns.corr(method='kendall'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[1])
    axes[1].set_title("Kendall")

    sns.heatmap(air_ns.corr(method='spearman'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[2])
    axes[2].set_title("Spearman")

    fig.patch.set_facecolor("#00172B")

    st.pyplot(fig)

    st.pyplot(sns.pairplot(data=air_ns, height=10, aspect=1))

elif check6:
    st.title('Rain')
    st.write('This is the second page of the app.')

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    fig.suptitle('Rain comparisons and correlation')

    sns.heatmap(rain_ns.corr(method='pearson'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[0])
    axes[0].set_title("Pearson")

    sns.heatmap(rain_ns.corr(method='kendall'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[1])
    axes[1].set_title("Kendall")

    sns.heatmap(rain_ns.corr(method='spearman'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[2])
    axes[2].set_title("Spearman")

    fig.patch.set_facecolor("#00172B")

    st.pyplot(fig)

    st.pyplot(sns.pairplot(data=rain_ns, height=10, aspect=1))




