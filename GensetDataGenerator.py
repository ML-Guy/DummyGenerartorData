import numpy as np

class GenSet:
	Time_Step = 0.25
	
	def __init__(self):
		self.Data = {
			"Overall_Data"	: {
				"Status"	: True
			},
			"Fuel_Data"	: {
				"Current_level"		: 97	,	#percentage of capacity
				"Consumption_rate"	: 73	,	#Liters/hour
				"Topup"				: 0		,	#Liters
				"Capacity"			: 850	,	#Liters
			},
			"Engine_Data"	: {
				"Temperature"	: 500	,	#Celcius
				"Oil_pressure"	: 0		,	#KPA
				"RPM"			: 1500	,
				"Engine_hours"	: 70	,
				"Num_starts"	: 8		,
			},
			"Battery_Data"	: {
				"Current_voltage"	:	23.5	,	#Volts		
			},
			"Power_Data"	: {
				"Voltage"	: { "R" : 415	, "Y" : 415		, "B" : 415		},	#Volts
				"Current"	: { "R" : 445.18, "Y" : 445.18	, "B" : 445.18	},	#Amps
				"KVA"		: { "R" : 106.67, "Y" : 106.67	, "B" : 106.67	},
				"KW"		: { "R" : 85.33	, "Y" : 85.33	, "B" : 85.33	},
				"KWAR"		: { "R" : 64.0	, "Y" : 64.0	, "B" : 64.0	},
			},
		}

	def next(self):
		#Independent Data w.r.t On/OFF state
		if np.random.rand() < 0.2 : 
			self.Data["Overall_Data"]["Status"]	= ~	self.Data["Overall_Data"]["Status"]	
			if self.Data["Overall_Data"]["Status"]:
				self.Data["Engine_Data"]["Num_starts"] += 1

		if np.random.rand() < 0.1 : 
			self.Data["Fuel_Data"]["Topup"]	= 100
		else:
			self.Data["Fuel_Data"]["Topup"]	= 0
		

		# Start state specific 
		if self.Data["Overall_Data"]["Status"]:
			self.Data["Fuel_Data"]["Consumption_rate"] += (np.random.rand()-0.5) * 4
			self.Data["Fuel_Data"]["Current_level"] += (self.Data["Fuel_Data"]["Topup"] -  self.Data["Fuel_Data"]["Consumption_rate"]* self.Time_Step)

			#Engine Data
			self.Data["Engine_Data"]["Temperature"]		= np.clip(self.Data["Engine_Data"]["Temperature"] + ((np.random.rand()) * 100),80,700)
			self.Data["Engine_Data"]["Oil_pressure"]	+= (np.random.rand()-0.5) * 2
			self.Data["Engine_Data"]["RPM"]				+= (np.random.rand()-0.5) * 20
			self.Data["Engine_Data"]["Engine_hours"]	+= self.Time_Step

			#Battery_Data
			self.Data["Battery_Data"]["Current_voltage"]= np.clip(self.Data["Battery_Data"]["Current_voltage"] + ((np.random.rand()) * 2),12,28)

			#Power_Data
			self.Data["Power_Data"] = {
				"Voltage"	: { "R" : 415	+((np.random.rand()-0.5) * 4), "Y" : 415	+((np.random.rand()-0.5) * 4), "B" : 415	+((np.random.rand()-0.5) * 4)},
				"Current"	: { "R" : 445.18+((np.random.rand()-0.5) * 4), "Y" : 445.18	+((np.random.rand()-0.5) * 4), "B" : 445.18 +((np.random.rand()-0.5) * 4)},
				"KVA"		: { "R" : 106.67+((np.random.rand()-0.5) * 4), "Y" : 106.67	+((np.random.rand()-0.5) * 4), "B" : 106.67 +((np.random.rand()-0.5) * 4)},
				"KW"		: { "R" : 85.33	+((np.random.rand()-0.5) * 4), "Y" : 85.33	+((np.random.rand()-0.5) * 4), "B" : 85.33	+((np.random.rand()-0.5) * 4)},
				"KWAR"		: { "R" : 64.0	+((np.random.rand()-0.5) * 4), "Y" : 64.0	+((np.random.rand()-0.5) * 4), "B" : 64.0	+((np.random.rand()-0.5) * 4)},
			}
		else:
		#Stop State specific Data
			self.Data["Fuel_Data"]["Consumption_rate"] += (np.random.rand()-0.5) * 4
			self.Data["Fuel_Data"]["Current_level"] += (self.Data["Fuel_Data"]["Topup"] -  self.Data["Fuel_Data"]["Consumption_rate"]* self.Time_Step)

			#Engine Data
			self.Data["Engine_Data"]["Temperature"]		= np.clip(self.Data["Engine_Data"]["Temperature"] - ((np.random.rand()) * 40),80,700)
			self.Data["Engine_Data"]["Oil_pressure"]	= 0
			self.Data["Engine_Data"]["RPM"]				= 0
			
			#Battery_Data
			self.Data["Battery_Data"]["Current_voltage"]= np.clip(self.Data["Battery_Data"]["Current_voltage"] - ((np.random.rand()) * 0.2),12,28)

			#Power_Data
			self.Data["Power_Data"] = {
				"Voltage"	: { "R" : 0, "Y" : 0 , "B" : 0 },
				"Current"	: { "R" : 0, "Y" : 0 , "B" : 0 },
				"KVA"		: { "R" : 0, "Y" : 0 , "B" : 0 },
				"KW"		: { "R" : 0, "Y" : 0 , "B" : 0 },
				"KWAR"		: { "R" : 0, "Y" : 0 , "B" : 0 },
			}

		return self.Data

g1 = GenSet()
print g1.Data
for i in range(20):
	print g1.next()