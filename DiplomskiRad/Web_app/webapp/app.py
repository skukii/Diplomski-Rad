#streamlit run app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

air_ns = pd.read_csv("pin_cop_ns_air_web - Copy.csv", index_col = [0])
rain_ns = pd.read_csv("pin_cop_ns_rain_web - Copy.csv", index_col = [0])
soil_ns = pd.read_csv("pin_cop_ns_soil_web - Copy.csv", index_col = [0])
temp_ns = pd.read_csv("pin_cop_ns_temp_web - Copy.csv", index_col = [0])

air_os = pd.read_csv("pin_cop_os_air_web - Copy.csv", index_col = [0])
rain_os = pd.read_csv("pin_cop_os_rain_web - Copy.csv", index_col = [0])
columns_helper = ["Speed [Pinova]", "Degrees [Pinova]", "Speed [Copernicus]", "Degrees [Copernicus]"]
wind_os = pd.read_csv("pin_cop_os_wind_web - Copy.csv", index_col = [0])[['wind-speed', 'pinova_degrees', 'u_v_speed', 'u_v_wind_dir']]
wind_os.rename(columns = {'wind-speed':'Speed [Pinova]', 'pinova_degrees': 'Direction [Pinova]', 'u_v_speed': 'Speed [Copernicus]', 'u_v_wind_dir': 'Direction [Copernicus]'}, inplace = True)
temp_os = pd.read_csv("pin_cop_os_temp_web - Copy.csv", index_col = [0])

air_bu = pd.read_csv("pin_cop_bu_air_web - Copy.csv", index_col = [0])
air_bu = air_bu[["Air moisture.mean", "humidity"]]
air_bu.dropna(inplace=True)
rad_bu = pd.read_csv("pin_cop_bu_radiation_web - Copy.csv", index_col = [0])
rad_bu.dropna(inplace=True)
rain_bu = pd.read_csv("pin_cop_bu_rain_web - Copy.csv", index_col = [0])
rain_bu.dropna(inplace=True)
temp_ground_bu = pd.read_csv("pin_cop_bu_temp_ground_web - Copy.csv", index_col = [0])
temp_ground_bu.dropna(inplace=True)
temp_bu = pd.read_csv("pin_cop_bu_temp_web - Copy.csv", index_col = [0])
temp_bu.dropna(inplace=True)
wind_bu = pd.read_csv("pin_cop_bu_wind_web - Copy.csv", index_col = [0])
wind_bu = wind_bu[["Wind speed.mean","Wind direction.mean","u_v_speed","u_v_wind_dir"]]
wind_bu.dropna(inplace=True)

air_sk = pd.read_csv("pin_cop_sk_air_web - Copy.csv", index_col = [0])
air_sk.dropna(inplace=True)
rad_sk = pd.read_csv("pin_cop_sk_radiation_web - Copy.csv", index_col = [0])
rad_sk.dropna(inplace=True)
rain_sk = pd.read_csv("pin_cop_sk_rain_web - Copy.csv", index_col = [0])
rain_sk.dropna(inplace=True)
temp_sk = pd.read_csv("pin_cop_sk_temp_web - Copy.csv", index_col = [0])
temp_sk.dropna(inplace=True)
wind_sk = pd.read_csv("pin_cop_sk_wind_web - Copy.csv", index_col = [0])
wind_sk = wind_sk[["Wind speed.mean","Wind direction.mean","u_v_speed","u_v_wind_dir"]]
wind_sk.dropna(inplace=True)



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
          "axes.labelsize":36
          }
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



def coefficients(df, col1, col2, alpha):
    corr_persons = stats.pearsonr(df[col1], df[col2])
    st.write("With hypothesis zero being: there is no correlation between two columns: ")

    if corr_persons[1] < (float(alpha)/2):
        st.write('2-tailed p-value Pearsons: ', corr_persons[1], '  (There is a statistically significant correlation)')
    else:
        st.write('2-tailed p-value Pearsons: ', corr_persons[1], '  (There is no statistically significant correlation)')

    with st.expander("See explanation for Pearson"):
        st.write("In statistics, the Pearson correlation coefficient is a measure of linear correlation between two sets of data. It is the ratio between the covariance of two variables and the product of their standard deviations")

    corr_kendall = stats.kendalltau(df[col1], df[col2])
    if corr_kendall[1] < (float(alpha)/2):
        st.write('2-tailed p-value Kendall: ', corr_kendall[1], '  (There is a statistically significant correlation)')
    else:
        st.write('2-tailed p-value Kendall: ', corr_kendall[1], '  (There is no statistically significant correlation)')

    with st.expander("See explanation for Kendall"):
        st.write("In statistics the Kendall rank correlation coefficient is a statistic used to measure the ordinal association between two measured quantities. A τ test is a non-parametric hypothesis test for statistical dependence based on the τ coefficient.")


    corr_spearmans = stats.spearmanr(df[col1], df[col2])
    if corr_spearmans[1] < (float(alpha)/2):
        st.write('2-tailed p-value Spearman: ', corr_spearmans[1], '  (There is a statistically significant correlation)')
    else:
        st.write('2-tailed p-value Spearman: ', corr_spearmans[1], '  (There is no statistically significant correlation)')

    with st.expander("See explanation for Spearman"):
        st.write("In statistics, Spearman's rank correlation coefficient or Spearman's ρ, is a nonparametric measure of rank correlation (statistical dependence between the rankings of two variables). It assesses how well the relationship between two variables can be described using a monotonic function.")


    st.write("##")
    x = df[col1]
    y = df[col2]
    mask = ~np.isnan(x) & ~np.isnan(y)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask], y[mask])
    st.write('Linear regression of 2 variables: ')
    st.write('Slope: ', slope)
    st.write('Intercept: ', intercept)
    st.write('R squared value: ', r_value*r_value)
    st.write('p-value: ', p_value)
    st.write('Standard error: ', std_err)

    with st.expander("See explanation for linear regression variables:"):
        st.write("Slope: Slope of the regression line.")
        st.write("Intercept: Intercept of the regression line.")
        st.write("R squared value: The square of rvalue is equal to the coefficient of determination.")
        st.write("p-value: The p-value for a hypothesis test whose null hypothesis is that the slope is zero, using Wald Test with t-distribution of the test statistic.")
        st.write("Standard error: Standard error of the estimated slope (gradient), under the assumption of residual normality.")




def heatmap(df, title):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    fig.suptitle(title)

    sns.heatmap(df.corr(method='pearson'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[0])
    axes[0].set_title("Pearson")

    sns.heatmap(df.corr(method='kendall'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[1])
    axes[1].set_title("Kendall")

    sns.heatmap(df.corr(method='spearman'), vmin=-1, vmax=1, center=0, annot=True, linewidth=4, ax=axes[2])
    axes[2].set_title("Spearman")
    fig.patch.set_facecolor("#00172B")
    st.pyplot(fig)

def pairplot(df):
    st.pyplot(sns.pairplot(data=df, height=10, aspect=1))


check = st.selectbox(
        "Analysis of:",
        ("Wind", "Temperature", "Soil", "Air conditions", "Rain"))


if check == "Wind":
    st.title('Wind')
    option = st.selectbox(
        "Location",
        ("Osijek", "Budimci", "Skenderovci"))

    if (option == "Osijek"):

        st.write(wind_os.describe())

        columns = wind_os.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))
        alpha = st.text_input('Set the significance level (alpha): ', '0.05')


        if ((option_one is not None) & (option_two is not None)):
            coefficients(wind_os, option_one, option_two, alpha)

        else:
            coefficients(wind_os, option_one, option_two, alpha)

        heatmap(wind_os, 'Wind comparisons and correlation')
        pairplot(wind_os)

    elif (option == "Budimci"):

        st.write(wind_bu.describe())

        columns = wind_bu.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))
        alpha = st.text_input('Set the significance level (alpha): ', '0.05')

        if ((option_one is not None) & (option_two is not None)):
            coefficients(wind_bu, option_one, option_two, alpha)

        else:
            coefficients(wind_bu, option_one, option_two, alpha)

        heatmap(wind_bu, 'Wind comparisons and correlation')
        pairplot(wind_bu)

    elif (option == "Skenderovci"):

        st.write(wind_sk.describe())

        columns = wind_sk.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(wind_sk, option_one, option_two, alpha)

        else:
            coefficients(wind_sk, option_one, option_two, alpha)

        heatmap(wind_sk, 'Wind comparisons and correlation')
        pairplot(wind_sk)

elif check == "Temperature":

    option = st.selectbox(
        "Location",
        ("Osijek", "Novi Rok", "Budimci", "Skenderovci"))

    st.title('Temperature')

    if (option == "Novi Rok"):

        st.write(temp_ns.describe())

        columns = temp_ns.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(temp_ns, option_one, option_two, alpha)

        else:
            coefficients(temp_ns, option_one, option_two, alpha)

        heatmap(temp_ns, 'Temperature comparisons and correlation')
        pairplot(temp_ns)


    elif(option == "Osijek"):

        st.write(temp_os.describe())

        columns = temp_os.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(temp_os, option_one, option_two, alpha)

        else:
            coefficients(temp_os, option_one, option_two, alpha)

        heatmap(temp_os, 'Temperature comparisons and correlation')
        pairplot(temp_os[["dew-pt", "dew2m", "temp2m", "temp-out"]])
        pairplot(temp_os[["max2mt", "min2mt", "hi-temp", "low-temp"]])


    elif (option == "Budimci"):

        st.write(temp_bu.describe())

        columns = temp_bu.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(temp_bu, option_one, option_two, alpha)

        else:
            coefficients(temp_bu, option_one, option_two, alpha)

        heatmap(temp_bu, 'Temperature comparisons and correlation')
        pairplot(temp_bu)

    elif (option == "Skenderovci"):

        st.write(temp_sk.describe())

        columns = temp_sk.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(temp_sk, option_one, option_two, alpha)

        else:
            coefficients(temp_sk, option_one, option_two, alpha)

        heatmap(temp_sk, 'Temperature comparisons and correlation')
        pairplot(temp_sk)

elif check == "Soil":
    st.title('Soil')

    option = st.selectbox(
        "Location",
        ("Novi Rok", "Budimci"))

    if (option == "Novi Rok"):

        st.write(soil_ns.describe())

        columns = soil_ns.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(soil_ns, option_one, option_two, alpha)

        else:
            coefficients(soil_ns, option_one, option_two, alpha)

        heatmap(soil_ns, 'Soil comparisons and correlation')
        pairplot(soil_ns)

    if (option == "Budimci"):

        st.write(temp_ground_bu.describe())

        columns = temp_ground_bu.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(temp_ground_bu, option_one, option_two, alpha)

        else:
            coefficients(temp_ground_bu, option_one, option_two, alpha)

        heatmap(temp_ground_bu, 'Soil comparisons and correlation')
        pairplot(temp_ground_bu)

elif check == "Air conditions":
    st.title('Air conditions')

    option = st.selectbox(
        "Location",
        ("Osijek", "Novi Rok", "Budimci", "Skenderovci"))

    if (option == "Osijek"):

        st.write(air_os.describe())

        columns = air_os.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(air_os, option_one, option_two, alpha)

        else:
            coefficients(air_os, option_one, option_two, alpha)

        heatmap(air_os, 'Air conditions comparisons and correlation')
        pairplot(air_os)

    elif (option == "Novi Rok"):

        st.write(air_ns.describe())

        columns = air_ns.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(air_ns, option_one, option_two, alpha)

        else:
            coefficients(air_ns, option_one, option_two, alpha)

        heatmap(air_ns, 'Air conditions comparisons and correlation')
        pairplot(air_ns)

    elif (option == "Budimci"):

        st.write(air_bu.describe())

        columns = air_bu.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(air_bu, option_one, option_two, alpha)

        else:
            coefficients(air_bu, option_one, option_two, alpha)

        heatmap(air_bu, 'Air conditions comparisons and correlation')
        pairplot(air_bu)

        columns2 = rad_bu.columns

        option_one2 = st.selectbox(
            "Column 1:",
            (columns2))
        option_two2 = st.selectbox(
            "Column 2:",
            (columns2))

        if ((option_one2 is not None) & (option_two2 is not None)):
            coefficients(rad_bu, option_one2, option_two2)

        else:
            coefficients(rad_bu, option_one2, option_two2)

        heatmap(rad_bu, 'Air conditions comparisons and correlation')
        pairplot(rad_bu)

    elif (option == "Skenderovci"):

        st.write(air_sk.describe())

        columns = air_sk.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(air_sk, option_one, option_two, alpha)

        else:
            coefficients(air_sk, option_one, option_two, alpha)

        heatmap(air_sk, 'Air conditions comparisons and correlation')
        pairplot(air_sk)

elif check == "Rain":
    st.title('Rain')

    option = st.selectbox(
        "Location",
        ("Osijek", "Novi Rok", "Budimci", "Skenderovci"))

    if(option == "Osijek"):

        st.write(rain_os.describe())

        columns = rain_os.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(rain_os, option_one, option_two, alpha)

        else:
            coefficients(rain_os, option_one, option_two, alpha)

        heatmap(rain_os, 'Rain conditions comparisons and correlation')
        pairplot(rain_os)

    elif(option == "Novi Rok"):

        st.write(rain_ns.describe())

        columns = rain_ns.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(rain_ns, option_one, option_two, alpha)

        else:
            coefficients(rain_ns, option_one, option_two, alpha)

        heatmap(rain_ns, 'Rain conditions comparisons and correlation')
        pairplot(rain_ns)


    elif (option == "Budimci"):

        st.write(rain_bu.describe())

        columns = rain_bu.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))

        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(rain_bu, option_one, option_two, alpha)

        else:
            coefficients(rain_bu, option_one, option_two, alpha)

        heatmap(rain_bu, 'Rain conditions comparisons and correlation')
        pairplot(rain_bu)

    elif (option == "Skenderovci"):

        st.write(rain_sk.describe())

        columns = rain_sk.columns

        option_one = st.selectbox(
            "Column 1:",
            (columns))
        option_two = st.selectbox(
            "Column 2:",
            (columns))
        alpha = st.text_input('Set the significance level (alpha): ', '0.05')
        if ((option_one is not None) & (option_two is not None)):
            coefficients(rain_sk, option_one, option_two, alpha)

        else:
            coefficients(rain_sk, option_one, option_two, alpha)

        heatmap(rain_sk, 'Rain conditions comparisons and correlation')
        pairplot(rain_sk)








