class WeibophonedockerPipeline:
    def __init__(self):
        self.phone_user = 1

    def process_item(self, item, spider):
        if spider.name == 'phone_user':
            self.phone_user += 1
            print(11111111111111111111111111111, self.phone_user)
            if self.phone_user % 10 == 0:
                print(self.phone_user)
        print(item)
