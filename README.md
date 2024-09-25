# Overview

Time-series and statistical analyses of historical bankruptcy data in the EU and U.S., supporting business risk management strategies related to market volatility and interest rates. Group project using SQL, Python (Pandas, NumPy and Scikit-Learn), with insights visualised in Looker Studio.

# Context

Risk management is an essential factor of an expansion strategy. For European or US firms looking to enter new markets, it is necessary to understand the different economic environments and associated risks of these new regions. Our project aims to uncover insights into the these environments by analysing historical bankruptcy data and investigating the correlation patterns between different macroeconomic indicators e.g. interest rates.

# Data Sources

Eurostat:
- Bankruptcies and Business Registrations (absolute and indexed) + Wages, salaries and employment https://ec.europa.eu/eurostat/databrowser/view/sts_rb_q__custom_11603248/default/table?lang=en
- Investment https://ec.europa.eu/eurostat/databrowser/view/sbs_na_sca_r2__custom_11607391/default/table?lang=en
- Nonfinancial corporate debt https://ec.europa.eu/eurostat/databrowser/view/nasa_10_f_bs__custom_11607565/default/table?lang=en
  

ECB:
- Cost of borrowing for corporations (interest rates)
  

UScourts.gov
- Business bankruptcy cases filed (Chapter 11) https://www.uscourts.gov/statistics/table/f/bankruptcy-filings/2024/03/31
  

SEC
- Financial statements data sets https://www.sec.gov/dera/data/financial-statement-data-sets
  

ONS
- Company Insolvency Statistics https://www.gov.uk/government/collections/company-insolvency-statistics-releases
  

OECD
- Non-financial corporations debt to surplus ratio https://data.oecd.org/corporate/non-financial-corporations-debt-to-surplus-ratio.htm#indicator-chart
  

IMF
- Non-financial corporate debt https://www.imf.org/external/datamapper/NFC_ALL@GDD/SWE

# Insights
- In Europe, interest rates have been stable but with a general decline from 2015 until 2022 when they started to increase quickly, due to rising inflation
- The spike in bankruptcies in 2022-Q3 could be a result of increased interest rates starting in 2022

![2024-09-25](https://github.com/user-attachments/assets/d8c616ad-ceb9-4360-b3a6-8caf68431d94)

(Absolute number of bankruptcies for Europe and the U.S. not entirely comparable, due to e.g. different bankruptcy laws, fewer large firms in the U.S)
- Looking at year on year variations, number of bankruptcies in the U.S. is significantly more volatile than in Europe in recent years
- This may reflect the fact that the U.S. put less bankruptcy prevention measures in place during COVID-19 and re-opened the economy earlier than European states

![2024-09-25 (1)](https://github.com/user-attachments/assets/e85a92c5-a603-4a34-8079-144d7d94680b)

![2024-09-25 (2)](https://github.com/user-attachments/assets/ea235141-badb-4cfb-80f8-88cfa6ed137c)







