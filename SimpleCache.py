CACHE_BOOL = True

class model_data_singleton(object):
    __instance = None

    def __new__(cls, usecache=CACHE_BOOL):
        if model_data_singleton.__instance is None:
            print(f'model_data_singleton first instantiation, usecache={usecache}')
            model_data_singleton.__instance = object.__new__(cls)
            model_data_singleton.__instance.data_model_one = None
            model_data_singleton.__instance.data_model_two = None
            model_data_singleton.__instance.compare_model = None
            model_data_singleton.__instance.cache = {}
            model_data_singleton.__instance.useCache = usecache

        return model_data_singleton.__instance

    def initializer(self, key):
        ''' this is the only method that user can customize for his model '''
        static_list = local_cache_for_static_data(self.useCache)
        first_date = None
        second_date = None
        if key == 'all':
            model_data_singleton.data_model_one = init_func(first_date)
            model_data_singleton.data_model_two = init_func(second_date)
        if key == 'first':
            model_data_singleton.data_model_one = model_generator(first_date)
        if key == 'second':
            model_data_singleton.data_model_two = model_generator(second_date)
        model_data_singleton.compare_model = model_compare(model_data_singleton.data_model_one, model_data_singleton.data_model_two)
        return [model_data_singleton.data_model_one, model_data_singleton.data_model_two,  model_data_singleton.compare_model]

    def set_all(self, data_model_one, data_model_two, compare_model):
        model_data_singleton.__instance.data_model_one = data_model_one
        model_data_singleton.__instance.data_model_two = data_model_two
        model_data_singleton.__instance.compare_model = compare_model
        self.__add_to_cache(data_model_one)
        self.__add_to_cache(data_model_two)
        self.__add_to_cache(compare_model)
        return self

    def get_all(self):
        if not self.useCache:
            model_one, model_two, compare_model = self.initializer('both')
            self.set_all(model_one, model_two, compare_model)
            return [
                model_data_singleton.__instance.data_model_one,
                model_data_singleton.__instance.data_model_two,
                model_data_singleton.__instance.compare_model]
        else:
            return [
                    self.cache[self.data_model_one],
                    self.cache[self.data_model_two],
                    self.cache[self.compare_model]
            ]

    def __add_to_cache(self, data):
        if model_data_singleton.__instance.useCache:
            self.cache[data] = data
        return self

    def __str__(self):
        return str([self.data_model_one, self.data_model_two, self.compare_model])

    def set_first(self, data_model_one):
        model_data_singleton.__instance.data_model_one = data_model_one
        self.__add_to_cache(data_model_one)
        return self

    def set_second(self, data_model_two):
        model_data_singleton.__instance.data_model_two = data_model_two
        self.__add_to_cache(data_model_two)
        return self

    def get_first(self):
        if not self.useCache:
            model_one, model_two, compare_model = self.initializer('first')
            self.set_all(model_one, model_two, compare_model)
        return [model_data_singleton.__instance.data_model_one]

    def get_second(self):
        if not self.useCache:
            model_one, model_two, compare_model = self.initializer('second')
            self.set_all(model_one, model_two, compare_model)
        return [model_data_singleton.__instance.data_model_two]


def local_cache_for_static_data(usecache):
    if not usecache:
        return model_trading_calendar()['trading_days'][:]
    else:
        if 'static_days' not in local_cache.keys():
            local_cache['static_days'] = generate_trading_calendar()['trading_days'][:]
        return local_cache['static_days']
