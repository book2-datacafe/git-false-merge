

### Book will be working on this project

##data prep

df_forecasted['local_arabica_y'] = df_forecasted.apply(lambda row: 0 if row['product_name'] == 'expensive' else (20*row['y'] if row['product_name'] == 'cheap' else 10* row['y']) , axis=1 )
df_forecasted['foreign_arabica_y'] = df_forecasted.apply(lambda row: 0 if row['product_name'] == 'cheap' else (10*row['y'] if row['product_name'] in ['medium','expensive'] else 0), axis=1)
df_forecasted['robusta_y'] = df_forecasted.apply(lambda row: 0 if row['product_name'] in ['cheap', 'medium'] else 10*row['y'], axis=1)

df_forecasted['local_arabica_yhat'] = df_forecasted.apply(lambda row: 0 if row['product_name'] == 'expensive' else (20*row['yhat'] if row['product_name'] == 'cheap' else 10* row['yhat']) , axis=1 )
df_forecasted['foreign_arabica_yhat'] = df_forecasted.apply(lambda row: 0 if row['product_name'] == 'cheap' else (10*row['yhat'] if row['product_name'] in ['medium','expensive'] else 0), axis=1)
df_forecasted['robusta_yhat'] = df_forecasted.apply(lambda row: 0 if row['product_name'] in ['cheap', 'medium'] else 10*row['yhat'], axis=1)

forecast_material.to_gbq(destination_table='datacafeplayground.total_supply_chain.table_forecast_material',
                         project_id='datacafeplayground',
                         if_exists='replace', #options -> 'fail' 'replace' 'append'
                         table_schema=[{'name': 'date', 'type': 'DATE'}]
                        )