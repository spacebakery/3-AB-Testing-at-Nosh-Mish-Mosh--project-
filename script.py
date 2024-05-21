import noshmishmosh
import numpy as np


all_visitors = noshmishmosh.customer_visits

paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

baseline_percentage = paying_visitor_count / total_visitor_count * 100
print("Baseline Convertion Rate: " + str(baseline_percentage))

payment_history = noshmishmosh.money_spent

average_payment = np.mean(payment_history)

new_customers_needed = np.ceil(1240 / average_payment)

percent_point_increase = new_customers_needed / total_visitor_count * 100
print("New Customers required as a percent of total visitors = " + str(percent_point_increase) + " %")

lift = percent_point_increase / baseline_percentage * 100
print("Lift: " + str(round(lift, 2)) + " %")

statistical_significance_percent = 90
print("Statistical Significance = "+ str(statistical_significance_percent)+ " %")

# 15
"""
Based on the Smaple Determination Calculator
"""
ab_sample_size = 494

# 16
print("The number of people (sample size) need to see the artisanal-looking vegetable section is " + str(ab_sample_size))
