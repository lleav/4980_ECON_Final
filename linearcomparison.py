import json
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pandas
import string
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn import preprocessing
from sklearn import utils
from sklearn import metrics
import nltk
from nltk.corpus import stopwords
from sklearn import tree
import matplotlib.pyplot as plt

data_name = []
data_stars = []
data_address = []
data_state = []
data_wi = []
data_nc = []
data_sc = []
data_va = []
data_ga = []
data_hours = []
data_sunday = []
data_sunday_close = []
data_appointment = []
data_restaurant_price = []
data_categories = []
data_first_category = []
data_restaurant = []
data_latitude = []
data_longitude = []
data_reservations = []
data_valet = []
data_street = []
data_garage = []
data_validated = []
data_lot = []
data_alcohol = []
data_delivery = []
data_kidfriendly = []
data_takeout = []
data_mexicanfood = []
data_wings = []
data_burgers = []
data_pizza = []
data_caters = []
data_casual = []
data_romantic = []
data_upscale = []
data_trendy = []
data_touristy = []
data_hipster = []
data_divey = []
data_intamate = []
data_classy = []
# data_postalcode = []

with open('business_sample.json', encoding="utf8") as f:
	for line in f:
		json_line = json.loads(line)

		cell_latitude = json_line.get('latitude')
		data_latitude.append(cell_latitude)

		cell_longitude = json_line.get('longitude')
		data_longitude.append(cell_longitude)

		# # To get the stars score
		cell_stars = json_line.get('stars')
		data_stars.append(cell_stars)

		
		# To get the state
		cell_state = json_line.get('state')
		data_state.append(cell_state)

		# # To get a variable indicating whether the business is in Wisconsin
		cell_wi = (cell_state == "WI")
		data_wi.append(cell_state == "WI")

		cell_nc = (cell_state == "NC")
		data_nc.append(cell_state == "NC")

		cell_sc = (cell_state == "SC")
		data_sc.append(cell_state == "SC")

		cell_va = (cell_state == "VA")
		data_va.append(cell_state == "VA")

		cell_ga = (cell_state == "GA")
		data_ga.append(cell_state == "GA")
		
		# # To get the opening time
		cell_hours = json_line.get('hours')
		data_hours.append(cell_hours)


		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_appointment = cell_attribute.get('ByAppointmentOnly')
			if cell_appointment is not None:
				data_appointment.append(1)
			else:
				data_appointment.append(0)
		else:
			data_appointment.append(0)

		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_reservations = cell_attribute.get('RestaurantsReservations')
			if cell_reservations is not None:
				if cell_reservations is True:
					data_reservations.append(1)
				else:
					data_reservations.append(0)
			else:
				data_reservations.append(0)
		else:
			data_reservations.append(0)
##parking dummy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_valet = cell_attribute.get('valet')
			if cell_valet is not None:
				if cell_valet is True:
					data_valet.append(1)
				else:
					data_valet.append(0)
			else:
				data_valet.append(0)
		else:
			data_valet.append(0)

		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_garage = cell_attribute.get('garage')
			if cell_garage is not None:
				if cell_garage is True:
					data_garage.append(1)
				else:
					data_garage.append(0)
			else:
				data_garage.append(0)
		else:
			data_garage.append(0)

		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_street = cell_attribute.get('street')
			if cell_street is not None:
				if cell_street is True:
					data_street.append(1)
				else:
					data_street.append(0)
			else:
				data_street.append(0)
		else:
			data_street.append(0)

		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_validated = cell_attribute.get('validated')
			if cell_validated is not None:
				if cell_validated is True:
					data_validated.append(1)
				else:
					data_validated.append(0)
			else:
				data_validated.append(0)
		else:
			data_validated.append(0)

		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_lot = cell_attribute.get('lot')
			if cell_lot is not None:
				if cell_lot is True:
					data_lot.append(1)
				else:
					data_lot.append(0)
			else:
				data_lot.append(0)
		else:
			data_lot.append(0)



	#alcohol dummy

		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_alcohol = cell_attribute.get('Alcohol')
			if cell_alcohol is not None:
				if cell_alcohol is True:
					data_alcohol.append(1)
				else:
					data_alcohol.append(0)
			else:
				data_alcohol.append(0)
		else:
			data_alcohol.append(0)
# delivery dummy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_delivery = cell_attribute.get('RestaurantsDelivery')
			if cell_delivery is not None:
				if cell_delivery is True:
					data_delivery.append(1)
				else:
					data_delivery.append(0)
			else:
				data_delivery.append(0)
		else:
			data_delivery.append(0)
#kidfriendlydummy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_kidfriendly = cell_attribute.get('GoodForKids')
			if cell_kidfriendly is not None:
				if cell_kidfriendly is True:
					data_kidfriendly.append(1)
				else:
					data_kidfriendly.append(0)
			else:
				data_kidfriendly.append(0)
		else:
			data_kidfriendly.append(0)
#takeout dummy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_takeout = cell_attribute.get('RestaurantsTakeOut')
			if cell_takeout is not None:
				if cell_takeout is True:
					data_takeout.append(1)
				else:
					data_takeout.append(0)
			else:
				data_takeout.append(0)
		else:
			data_takeout.append(0)
#cater dummy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_caters = cell_attribute.get('Caters')
			if cell_caters is not None:
				if cell_caters is True:
					data_caters.append(1)
				else:
					data_caters.append(0)
			else:
				data_caters.append(0)
		else:
			data_caters.append(0)
#environment dummies
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_casual = cell_ambiance.get('casual')
				if cell_casual is True:
					data_casual.append(1)
				else:
					data_casual.append(0)
			else:
				data_casual.append(0)
		else:
			data_casual.append(0)

		#upscale
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_upscale = cell_ambiance.get('upscale')
				if cell_upscale is True:
					data_upscale.append(1)
				else:
					data_upscale.append(0)
			else:
				data_upscale.append(0)
		else:
			data_upscale.append(0)

		#trendy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_trendy = cell_ambiance.get('trendy')
				if cell_trendy is True:
					data_trendy.append(1)
				else:
					data_trendy.append(0)
			else:
				data_trendy.append(0)
		else:
			data_trendy.append(0)
		#divey
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_divey = cell_ambiance.get('divey')
				if cell_divey is True:
					data_divey.append(1)
				else:
					data_divey.append(0)
			else:
				data_divey.append(0)
		else:
			data_divey.append(0)
		#touristy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_touristy = cell_ambiance.get('touristy')
				if cell_touristy is True:
					data_touristy.append(1)
				else:
					data_touristy.append(0)
			else:
				data_touristy.append(0)
		else:
			data_touristy.append(0)
		#romantic
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_romantic = cell_ambiance.get('romantic')
				if cell_romantic is True:
					data_romantic.append(1)
				else:
					data_romantic.append(0)
			else:
				data_romantic.append(0)
		else:
			data_romantic.append(0)
		#intimate
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_intimate = cell_ambiance.get('intimate')
				if cell_intimate is True:
					data_intamate.append(1)
				else:
					data_intamate.append(0)
			else:
				data_intamate.append(0)
		else:
			data_intamate.append(0)
		#classy
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_classy = cell_ambiance.get('classy')
				if cell_classy is True:
					data_classy.append(1)
				else:
					data_classy.append(0)
			else:
				data_classy.append(0)
		else:
			data_classy.append(0)
	#hipster
		cell_attribute = json_line.get('attributes')
		if cell_attribute is not None:
			cell_ambiance = cell_attribute.get('Ambiance')
			if cell_ambiance is not None:
				cell_hipster = cell_ambiance.get('hipster')
				if cell_hipster is True:
					data_hipster.append(1)
				else:
					data_hipster.append(0)
			else:
				data_hipster.append(0)
		else:
			data_hipster.append(0)




		# # To get restaurant price range, 'None' if the business did not specified that of it does not have any attributes.
		if cell_attribute is not None:
			cell_restaurant_price = cell_attribute.get('RestaurantsPriceRange2')
			if cell_restaurant_price == 1:
				data_restaurant_price.append(1)
			else:
				if cell_restaurant_price == 2:
					data_restaurant_price.append(2)
				else:
					if cell_restaurant_price == 3:
						data_restaurant_price.append(3)
					else:
						data_restaurant_price.append(0)	
		else:
			data_restaurant_price.append(0)

		# # To get all the categories
		cell_categories = json_line.get('categories')
		data_categories.append(cell_categories)

		# # To get only the first category
		if cell_categories is not None:
			cell_first_category = cell_categories.split(', ')[0]
			data_first_category.append(cell_first_category)
		else:
			data_first_category.append(None)


		# # To get a variable indicating whether 'restaurant' is one of the items in categories. 
		if cell_categories is not None:
			cell_restaurant = ('Restaurants' in cell_categories)
			data_restaurant.append(1)
		else:
			data_restaurant.append(0)
#food type dummies
		if cell_categories is not None:
			cell_mexicanfood = ('Mexican' in cell_categories)
			data_mexicanfood.append(1)
		else:
			data_mexicanfood.append(0)

		if cell_categories is not None:
			cell_wings = ('Chicken Wings' in cell_categories)
			data_wings.append(1)
		else:
			data_wings.append(0)

		if cell_categories is not None:
			cell_burgers = ('Burgers' in cell_categories)
			data_burgers.append(1)
		else:
			data_burgers.append(0)

		if cell_categories is not None:
			cell_pizza = ('Pizza' in cell_categories)
			data_pizza.append(1)
		else:
			data_pizza.append(0)

		
dataset = pandas.DataFrame(data={'stars':  data_stars,
								# 'name':  data_name, 
								# 'address': data_address,
								# 'state': data_state,
								'WI': data_wi,
								'NC': data_nc,
								'SC': data_sc,
								'GA': data_ga,
								'VA': data_va,
								# 'hours': data_hours,
								# 'sunday': data_sunday,
								# 'sunday_close_time': data_sunday_close,
								# 'by_appointment_only': data_appointment,
								# 'postal_code': data_postalcode,
								'restaurant_price': data_restaurant_price,
								# 'categories': data_categories,
								# 'first_category': data_first_category,
								'restaurant': data_restaurant,
								'latitude': data_latitude,
								'longitude': data_longitude,
								'reservations': data_reservations,
								'valet': data_valet,
								'alcohol':data_alcohol,
								'delivery': data_delivery,
								'kidfriendly': data_kidfriendly,
								'takeout': data_takeout,
								'mexicanfood': data_mexicanfood,
								'wings': data_wings,
								'burgers': data_burgers,
								'pizza': data_pizza,
								'caters': data_caters,
								'casual': data_casual,
								'classy': data_classy,
								'romantic': data_romantic,
								'upscale': data_upscale,
								'trendy': data_trendy,
								'hipster': data_hipster,
								'intimate': data_intamate,
								'touristy': data_touristy,
								'divey': data_divey,
								'lot' : data_lot,
								'validated': data_validated,
								'garage': data_garage,
								'street': data_street,
								})

dataset = dataset.round({'stars': 0})

target = dataset.iloc[:,0].values
data = dataset.iloc[:,1:33].values


data_training, data_test, target_training, target_test = train_test_split(data, target, test_size= 0.25)
machine = linear_model.LinearRegression()
machine.fit(data_training, target_training)
prediction = machine.predict(data_test)

print(metrics.r2_score(target_test, prediction))





