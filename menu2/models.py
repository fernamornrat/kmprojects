from django.db import models

class PPE(models.Model):
    ####################### อุปกรณ์ป้องกันอันตรายส่วนบุคคล #############################
    PPE_CHOICES = (
                    ('อุปกรณ์ป้องกันศีรษะ', 'อุปกรณ์ป้องกันศีรษะ'),               #'Head Protection Equipment'
                    ('อุปกรณ์ป้องกันใบหน้าและตา', 'อุปกรณ์ป้องกันใบหน้าและตา'),   #'Eye and face protection equipment'
                    ('อุปกรณ์ป้องกันหู', 'อุปกรณ์ป้องกันหู'),                     #'Ear protection equipment'
                    ('อุปกรณ์ป้องกันการหายใจ', 'อุปกรณ์ป้องกันการหายใจ'),        #'Respiratory protection equipment'
                    ('อุปกรณ์ป้องกันลำตัว', 'อุปกรณ์ป้องกันลำตัว'),                #'Body Protection Equipment'
                    ('อุปกรณ์ป้องกันมือ', 'อุปกรณ์ป้องกันมือ'),                   #'Hand Protection Equipment'
                    ('อุปกรณ์ป้องกันเท้า', 'อุปกรณ์ป้องกันเท้า'),                  #'Foot Protection Equipment'
    )
    name = models.CharField(max_length=200)
    ppe_sign = models.ImageField(upload_to='PPE_SIGN/%Y/%m/%d', blank=True)
    ppe_type = models.CharField(max_length=50, choices=PPE_CHOICES)

    def __str__(self):
        return self.name

class Experiment(models.Model):
    ################################ ระดับชั้น #######################################
    DEGREE_CHOICES = (
                        ('มัธยมศึกษาตอนต้น', 'มัธยมศึกษาตอนต้น'),     #'Middle School'
                        ('มัธยมศึกษาตอนปลาย', 'มัธยมศึกษาตอนปลาย'), #'High School'
    )
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)

    ################################ รายวิชา ########################################
    COURSE_CHOICES = (
                        ('ฟิสิกส์', 'ฟิสิกส์'),                          #'Physics'
                        ('เคมี', 'เคมี'),                              #'Chemistry'
                        ('ชีววิทยา', 'ชีววิทยา'),                       #'Biology'
                        ('โครงงานวิทยาศาสตร์', 'โครงงานวิทยาศาสตร์'),    #'Project science'
    )
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    course_number = models.CharField(max_length=50)

    ################################ หนังสือ ########################################
    book_name = models.CharField(max_length=200)
    book_number = models.CharField(max_length=50)

    ############################### การทดลอง #######################################
    experiment_number = models.CharField(max_length=50)
    experiment_name = models.CharField(max_length=200)

    ############################## สารเคมีที่ใช้ #######################################
    chemical_name_1 = models.CharField(max_length=200)
    chemical_name_2 = models.CharField(max_length=200)
    chemical_name_3 = models.CharField(max_length=200, blank=True)
    chemical_name_4 = models.CharField(max_length=200, blank=True)
    chemical_name_5 = models.CharField(max_length=200, blank=True)

    ############################## คุณสมบัติของสารเคมี #################################
    chemical_properties_1 =  models.CharField(max_length=1000)
    chemical_properties_2 =  models.CharField(max_length=1000)
    chemical_properties_3 =  models.CharField(max_length=1000, blank=True)
    chemical_properties_4 =  models.CharField(max_length=1000, blank=True)
    chemical_properties_5 =  models.CharField(max_length=1000, blank=True)

    ############################## สัญลักษณ์GHS #######################################
    GHS_CHOICES = (
                    ('สารไวไฟ', 'สารไวไฟ'),                              #'Flame'
                    ('สารออกซิไดซ์', 'สารออกซิไดซ์'),                      #'Flame Over Circle'
                    ('วัตถุระเบิด', 'วัตถุระเบิด'),                            #'Exploding Bomb'
                    ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'),       #'Gas Cylinder'
                    ('สารกัดกร่อน', 'สารกัดกร่อน'),                         #'Corrosion'
                    ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'),                       #'Skull & Crossbones'
                    ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'),                #'Health Hazard'
                    ('ระวัง', 'ระวัง'),                                     #'Exclamation Mark'
                    ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม'),            #'Environment'
    )
    ghs_sign_1 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d')
    ghs_name_1 = models.CharField(max_length=50, choices=GHS_CHOICES)

    ghs_sign_2 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_2 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ghs_sign_3 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_3 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ghs_sign_4 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_4 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ghs_sign_5 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_5 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ghs_sign_6 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_6 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ghs_sign_7 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_7 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ghs_sign_8 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_8 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ghs_sign_9 = models.ImageField(upload_to='GHS_SIGN/%Y/%m/%d', null=True)
    ghs_name_9 = models.CharField(max_length=50, choices=GHS_CHOICES, null=True)

    ####################### อุปกรณ์ป้องกันอันตรายส่วนบุคคล ###################################
    equipment = models.ForeignKey(PPE, on_delete=models.CASCADE)
    '''PPE_CHOICES = (
                    ('อุปกรณ์ป้องกันศีรษะ', 'อุปกรณ์ป้องกันศีรษะ'),               #'Head Protection Equipment'
                    ('อุปกรณ์ป้องกันใบหน้าและตา', 'อุปกรณ์ป้องกันใบหน้าและตา'),   #'Eye and face protection equipment'
                    ('อุปกรณ์ป้องกันหู', 'อุปกรณ์ป้องกันหู'),                     #'Ear protection equipment'
                    ('อุปกรณ์ป้องกันการหายใจ', 'อุปกรณ์ป้องกันการหายใจ'),        #'Respiratory protection equipment'
                    ('อุปกรณ์ป้องกันลำตัว', 'อุปกรณ์ป้องกันลำตัว'),                #'Body Protection Equipment'
                    ('อุปกรณ์ป้องกันมือ', 'อุปกรณ์ป้องกันมือ'),                   #'Hand Protection Equipment'
                    ('อุปกรณ์ป้องกันเท้า', 'อุปกรณ์ป้องกันเท้า'),                  #'Foot Protection Equipment'
    )
    name = models.CharField(max_length=200)
    ppe_type = models.CharField(max_length=50, choices=PPE_CHOICES)'''

    ####################### ความเป็นอันตรายที่เกี่ยวข้องกับการทดลอง #############################
    hazards = models.TextField()

    ######################## การทิ้งของเสีย ################################################
    w1 = models.CharField(max_length=100)
    w2 = models.CharField(max_length=100)
    w3 = models.CharField(max_length=100)
    w4 = models.CharField(max_length=100)
    w5 = models.CharField(max_length=100)
    w6 = models.CharField(max_length=100)
    w7 = models.CharField(max_length=100)
    wx = models.CharField(max_length=100)

    ####################### กลุ่มของของเสีย ################################################
    waste_group_w1 = models.CharField(max_length=1000)
    waste_group_w2 = models.CharField(max_length=1000)
    waste_group_w3 = models.CharField(max_length=1000)
    waste_group_w4 = models.CharField(max_length=1000)
    waste_group_w5 = models.CharField(max_length=1000)
    waste_group_w6 = models.CharField(max_length=1000)
    waste_group_w7 = models.CharField(max_length=1000)
    waste_group_wx = models.CharField(max_length=1000)

    ############## ข้อแนะนำเพิ่มเติมเกี่ยวข้องกับการจัดการของเสียอันตรายจากการทดลอง #################
    suggestion = models.TextField()

    def __str__(self): 
        return self.experiment_name