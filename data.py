weekDays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

schCalls = '1. 8:30 - 10:00\n2. 10:10 - 11:40\n3. 12:00 - 13:30\n4. 13:40 - 15:10\n5. 15:20 - 16:50\n6. 17:00 - 18:30\n7. 18:40 - 20:10\n8. 20:15 - 21:45\n'

idGroups = {'151502ОБ': 4888, '61ЭЭ': 4934, '61КШ-м': 5008, '31-ИК': 4165, '71ТЭ-мв': 6062, '51-НТС': 3616, '71ИК': 5710, 
	'71УТ-в': 5998, '71Ю': 5726, '74Ю': 5880, '71ГС': 5814, '41-ТП': 4049, '41-ИК': 4018, '41-НТС': 4059, '61ИН-мв': 5110, 
	'72ТД': 5883, '61Э-мв': 5113, '091405ОБ': 4693, '71ПИ': 5708, '61Э': 4945, '41-С': 4014, '71ТП-м': 5770, '41Ф': 4029, 
	'71ЭЭ-в': 5832, '071506ОС': 4629, '71АР': 5705, '61П': 5055, '61БС': 4933, '71ДЗ-в': 5839, '33-Ю': 4224, '61ТД': 4977, 
	'151404ОБ': 4896, '72Э': 5992, '61ТП-в': 5146, '131510ОБ': 4836, '71ТШ': 5718, '61П-м': 4994, '65Ю': 5187, '31-КТп': 4174, 
	'31-ПЖп': 4180, '4-ГУ': 4048, '42-С': 4064, '41-БС': 4025, '71Ф': 5827, '71Б-в': 5828, '091504ОБ': 4692, '71УТ': 5820, 
	'091305ОБ': 4694, '71ЭЭ-м': 5971, '3-КЭ': 4212, '41-Э': 4026, '72АР': 5986, '71МШ-м': 5984, '31-ТЭ': 4189, '41-ТОп': 4045, 
	'41-Ю': 4032, '71ПИ-в': 5830, '61ИВТ': 5053, '61ДА': 5070, '41-ТГ': 4046, '081501ОБ': 4644, '71ВСЭ-в': 5994, '31-ГД': 4159, 
	'61Р': 5054, '071502ОБ': 4615, '71С-м': 5759, '151302ОБ': 4891, '61ПР': 5058, '31-Э': 4173, '61ПЖ': 5059, '081506ОБ': 4660, 
	'71П': 5816, '61БТ-м': 4999, '61БИ': 4947, '5-1': 3592, '61АР': 4926, '71БИ-мв': 5851, '091404ОБ': 4683, '41-ВТп': 4004, 
	'61КЭ': 4932, '61Ф': 5071, '61БТ': 4935, '61С-м': 4990, '091503ОБ': 4679, '71НТС': 5975, '4-ПИ': 4047, '71БТ-м': 5767, 
	'71КЭ': 5711, '61ГУ': 4946, '131414ОБ': 4844, '71ТД': 5746, '61КТ-м': 4997, '71КТ': 5974, '71УК-м': 5969, '42-ЭТп': 4007, 
	'71КШ': 5719, '71ГУ-в': 5993, '61УТ-в': 5078, '71УТ-м': 5970, '61ТО-м': 4995, '31-ВТп': 4152, '32-АР': 4210, '091401ОБ': 4680, 
	'71ПР': 5817, '41-ЭО': 4009, '071504ОБ': 4624, '61ПГ-м': 4992, '62ТД': 5189, '081403ОБ': 4651, '61ИН-м': 5007, '71ИКТ': 5740, 
	'61ГС': 5052, '31-ЭО': 4157, '31-БС': 4172, '61ТГ': 5064, '61-СУ': 3166, '32-ТД': 4309, '61М-м': 5012, '41-МХп': 4052, 
	'71ПГОфк': 5976, '71Ю-в(у)': 6063, '31-ТТ': 4168, '61БД-м': 5047, '61МХ': 5057, '31-ТД': 4167, '31-ТГ': 4193, '4-КЭ': 4065, 
	'41-КЭ': 4061, '61ПЖ-м': 5001, '41-ИТ': 4044, '151504ОБ': 4895, '71ПГ': 5709, '31-ТБ': 4183, '71ЭТ': 5717, '61ИКТ': 4970, 
	'71ДА-м': 5801, '71ТТ-м': 5772, '71ИН-м': 5775, '71ИВТ': 5815, '31-ПРп': 4216, '071405ОБ': 4636, '71УП': 5822, '61УТ': 5061, 
	'41-АПп': 4037, '42-АР': 4063, '081401ОБ': 4645, '5-3': 3600, '3-ПИ': 4194, '71ПР-м': 5768, '081502ОБ': 4650, '71ИТ': 5707, 
	'61С': 4927, '31-КШ': 4181, '41-ЭТ': 4008, '71БД-м': 5810, '31-НТС': 4206, '61ЭБ': 4976, '41-КТп': 4027, '71ТГ-мв': 5852, 
	'5-4': 3660, '63Ю': 5185, '61ТБ': 4936, '71КЭ-м': 5762, '61УК-мз': 5109, '72ТБ': 5988, '61КЭ-м': 4993, '71ФК-мв': 6065, 
	'51-ПК': 3618, '72КЭ-м': 5882, '61Х': 4922, '52-ТД': 3728, '51-ТД': 3568, '61ТЭ': 5065, '61ГД-мз(кл)': 5133, '42-Ю': 4076, 
	'61ТБ-мз': 5108, '41-ПРп': 4069, '31-М': 4190, '081505ОБ': 4664, '41-ПЖп': 4033, '31-ПБ': 4198, '61ПР-м': 5000, '31-ПИ': 4201, 
	'41-М': 4043, '41-ЭБ': 4073, '71С': 5706, '61ТЭ-в': 5151, '61СП-мз': 5143, '52-АР': 3730, '081404ОБ': 4655, '71С-в': 5829, 
	'61ИК': 4931, '31-Рп': 4207, '71ПЖ': 5818, '61ЭТ-в': 5077, '091403ОБ': 4682, '71Х': 5702, '31-Пп': 4266, '61ПИ-в': 5074, 
	'41-АР': 4050, '71Ю-м': 5786, '61ТТ': 4937, '71ДЗ-мв': 5873, '71М-мв': 5848, '61Ю': 4949, '31-С': 4265, '61АП-м': 4996, 
	'61ТШ': 4941, '42-Э': 4072, '31-РК': 4262, '71ТБ': 5715, '61ИТ': 4928, '61ТП-м': 5002, '71ПГ-м': 5761, '41-ТД': 4020, 
	'41-МШп': 4041, '43-ЭБ': 4075, '41-ПМп': 4058, '31-ПМп': 4205, '71БС-м': 5978, '71М-м': 5780, '3-ЭЭ': 4213, '61ДА-м': 5038, 
	'4-УТ': 4068, '31-ДЗ': 4202, '41-ДЗ': 4055, '71ТГ': 5823, '71ИБ': 5977, '71ЭЭ': 5713, '32-Ю': 4223, '31-ТОп': 4192, 
	'61МХ-м': 4998, '61М': 5062, '61АР-мв': 5104, '61Б-в': 5072, '71ЭТ-м': 5774, '31-КЭ': 4208, '091501ОБ': 4677, '61УП': 5063, 
	'71Ю-мв': 5858, '41-ПГ': 4003, '71ТП': 5819, '151401ОБ': 4885, '71ЭТ-в': 5833, '31-ИТ': 4191, '61ТГ-м': 5016, '61Ю-м': 5022, 
	'31-ТУ': 4269, '71АР-м': 5989, '32-С': 4211, '61М-мв': 5115, '61ТП': 5060, '61Ю-мв': 5125, '61ТГ-мв': 5119, '71Э': 5722, 
	'71Ю-в': 5838, '131514ОБ': 4843, '131413ОБ': 4840, '31-МШп': 4188, '151505ОБ': 4897, '4-ДЗ': 4082, '32-ЭТп': 4155, '081405ОБ': 4661, 
	'71МХ': 5973, '31-МХп': 4199, '62ЭТ': 5156, '71ТТ': 5716, '31-ЭБ': 4220, '71Э-мв': 5846, '41-КШ': 4034, '71ЭБ': 5745, '71МХ-м': 5766, 
	'071501ОБ': 4610, '081406ОБ': 4665, '61НТ-м': 5005, '71СП-м': 5807, '31-АР': 4197, '71ИН-мв': 5843, '4-ЭТ': 4067, '71УК': 5983, 
	'72ЭБ': 5987, '62КЭ-м': 5188, '3-ЭТ': 4214, '61ТТ-м': 5004, '3-УТ': 4215, '31-У': 4178, '071505ОС': 4626, '71Э-м': 5779, '73Ю': 5879, 
	'71УП-мв': 6064, '41-ПИ': 4054, '71М': 5821, '61М-в': 5148, '31-ПГ': 4151, '42-ЭБ': 4074, '71КТ-м': 5765, '61Э-м': 5011, '64ТД': 5191, 
	'71М-в': 5876, '61ЭЭ-мз': 5107, '61КТ': 5056, '71АП-м': 5764, '71ТО-м': 5763, '71ПИ-м': 5760, '5-2': 3596, '091502ОБ': 4678, 
	'43-Ю': 4077, '31-АПп': 4184, '61БИ-мв': 5118, '71ГУ': 5723, '61ЭЭ-в': 5076, '41-Рп': 4060, '61ЭТ-м': 5006, '71ПГОфк-м': 5982, 
	'64Ю': 5186, '61БИ-м': 5015, '61КШ': 4942, '62Ю': 5184, '4-ЭЭ': 4066, '3-ТП': 4270, '41-УП': 4024, '61ПИ-м': 4991, '61ПГ': 4930, 
	'31-ТП': 4196, '71ПЖ-м': 5769, '51-АР': 3598, '72С-м': 5985, '71БИ': 5724, '091402ОБ': 4681, '41-ТТ': 4021, '071403ОБ': 4621, 
	'41-У': 4031, '34-Ю': 4312, '61ПИ': 4929, '41-ТЭ': 4042, '61НТ': 4938, '081503ОБ': 4654, '41-ГД': 4011, '63ТД': 5190, '71КЭ-в': 5831, 
	'151501ОБ': 4884, '41-ПБ': 4051, '31-ЭТ': 4156, '071503ОБ': 4620, '41-ТБ': 4036, '71КШ-м': 5776, '31-Ю': 4179, '081402ОБ': 4646, 
	'71НТ-м': 5773, '61КЭ-в': 5075, '71АП': 5972, '081504ОБ': 4658, '61С-в': 5073, '131513ОБ': 4839, '71БТ': 5714, '31Ф': 4176, '72Ю': 5878}

idFaculties = {'ХГФ': 159, 'ПТИ': 124, 'АСИ': 5, 'ФКС': 26, 'ИЭиУ': 289, 'ЮИ': 2, 'ИВЗО': 12, 'ФЕН': 152, 'ИПАИТ': 7, 'ИБиБ': 11}