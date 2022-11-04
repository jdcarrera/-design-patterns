class Singleton_example(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            instance = super().__call__(*args, **kwargs)
            cls.instances[cls] = instance
        return cls.instances[cls]

class Singleton(metaclass=Singleton_example):
    def some_business_logic(self):
        
        if __name__ == "__main__":
            s1 = Singleton()
            s2 = Singleton()

        if id(s1) == id(s2):
            print("Singleton works, both variables contain the same instance.")
        else:
            print("Singleton failed, variables contain different instances.")