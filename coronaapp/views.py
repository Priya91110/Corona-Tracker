from django.shortcuts import render
import requests, pandas as pd, json
from sqlalchemy import create_engine
# def get_conn():
#     try:
#         engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')
#         return  engine
#     except:
#         print("connection failed")
#     return None
def corona_data(request):
    country = request.GET.get('country', 'india')
    url = f'https://disease.sh/v3/covid-19/countries/{country}'
    response = requests.get(url)
    if response.status_code == 200:
        # con= get_conn()
        data = response.json()
        # print(data)
        df = pd.DataFrame(data)
        df.drop(['updated','countryInfo','todayCases', 'todayDeaths', 'todayRecovered','casesPerOneMillion', 'deathsPerOneMillion', 'testsPerOneMillion', 'oneCasePerPeople','oneDeathPerPeople', 'oneTestPerPeople', 'activePerOneMillion','recoveredPerOneMillion', 'criticalPerOneMillion'], axis=1, inplace=True)
        # print(df)
        # print(df.columns)
        # df.drop(["_id","iso2","iso3","lat","long","flag"], axis=0, inplace=True)
        # print(df)
        # print(df.columns)
        # print(df)
        # ['country', 'cases', 'deaths', 'recovered', 'active', 'critical',
    #    'tests', 'population', 'continent'],
        # print(df.dtypes)
        mydict={
            'deaths': data['deaths'],
            'country': data["country"],
            'cases': data['cases'],
            'recovered': data["recovered"],
            'active': data["active"],
            'critical': data["critical"],
            'tests': data["tests"],
            'population': data["population"],
            'continent': data["continent"],
        }
        # df.to_sql("coronaupdate",con=con, schema="apis", if_exists="append", index=False)
    else:
        print(f'Failed to retrieve COVID-19 data for {country}.')
    return render(request, "coronaapp/index.html",{"mydict":mydict})
