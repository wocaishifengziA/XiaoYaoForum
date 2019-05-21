import datetime
import json
from XiaoYaoForm.handler import RedisHandler
from apps.users.forms import SmsCodeForm


class SmsHandler(RedisHandler):
    # def generate_code(self):
    #     """
    #     生成随机4位数字的验证码
    #     :return:
    #     """
    #     seeds = "1234567890"
    #     random_str = []
    #     for i in range(4):
    #         random_str.append(choice(seeds))
    #     return "".join(random_str)

    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode("utf-8")
        param = json.loads(param)
        sms_form = SmsCodeForm.from_json(param)
        # if sms_form.validate():
        #     mobile = sms_form.mobile.data
        #     code = self.generate_code()
        #     yun_pian = AsyncYunPian("d6c4ddbf50ab36611d2f52041a0b949e")
        #
        #     re_json = await yun_pian.send_single_sms(code, mobile)
        #     if re_json["code"] != 0:
        #         self.set_status(400)
        #         re_data["mobile"] = re_json["msg"]
        #     else:
        #         #将验证码写入到redis中
        #         self.redis_conn.set("{}_{}".format(mobile,code), 1, 10*60)
        # else:
        #     self.set_status(400)
        #     for field in sms_form.errors:
        #         re_data[field] = sms_form.errors[field][0]
        #
        # self.finish(re_data)