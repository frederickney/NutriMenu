import Pollers


__F2F_TEA_SPOON_VALUE__ = 5
__F2F_TABLE_SPOON_VALUE__ = 15
__F2F_CUP_VALUE__ = 250
__F2F_ONCE_VALUE__ = 28.3
__F2F_TEA_SPOON__ = " teaspoon "
__F2F_TABLE_SPOON__ = " tablespoon "
__F2F_CUP__ = " cup "
__F2F_ONCE_ = " once "
__F2F_TEA_SPOONS__ = " teaspoons "
__F2F_TABLE_SPOONS__ = " tablespoons "
__F2F_CUPS__ = " cups "
__F2F_ONCES_ = " onces "


class Get_dish(object):

	def __init__(self, id):
		self.id = id
		request = Pollers.F2F_poller(id)
		if not request['recipe']:
			self.dish = None
			self.ingredients = None
		else:
			self.dish = request['recipe']['title']
			self.ingredients = self.__process__(request['recipe']['ingredients'])
		return

	def __process__(self, ingredients):
		ingredients_tmp = []
		for ingredient in ingredients:
			ingredient_tmp.append(self.__unit_converter__(ingredient))
		return ingredients_tmp
	
	def __unit_converter__(self, ingredient):
		splited_ingredient = str.split(ingredient)
		return