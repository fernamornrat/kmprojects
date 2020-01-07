from django.contrib import admin
from menu2.models import PPE, Experiment

class PPEAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ppe_type', 'ppe_sign')
    list_display_links = ('id','name')
    list_filter = ['ppe_type']
    search_fields = ('id','name')

admin.site.register(PPE,PPEAdmin)

class ExperimentAdmin(admin.ModelAdmin):
    fieldsets = [
        ###################################### เกี่ยวกับรายวิชา ####################################################
        ('About a Course',                      {'fields': ['degree','course','course_number','book_name','book_number']}),
        
        ####################################### การทดลอง #######################################################
        ('Experiment',                          {'fields': ['experiment_number', 'experiment_name']}),

        ####################################### สารเคมีที่ใช้ #######################################################
        ('Chemicals used',                      {'fields': ['chemical_name_1', 'chemical_properties_1',
                                                            'chemical_name_2', 'chemical_properties_2',
                                                            'chemical_name_3', 'chemical_properties_3',
                                                            'chemical_name_4', 'chemical_properties_4',
                                                            'chemical_name_5', 'chemical_properties_5']}),
                                                   
        ('GHS Sign',                            {'fields': ['ghs_sign_1', 'ghs_name_1',
                                                            'ghs_sign_2', 'ghs_name_2',  
                                                            'ghs_sign_3', 'ghs_name_3',  
                                                            'ghs_sign_4', 'ghs_name_4', 
                                                            'ghs_sign_5', 'ghs_name_5',
                                                            'ghs_sign_6', 'ghs_name_6', 
                                                            'ghs_sign_7', 'ghs_name_7', 
                                                            'ghs_sign_8', 'ghs_name_8', 
                                                            'ghs_sign_9', 'ghs_name_9']}),

        
        ####################################### อุปกรณ์ป้องกันอันตราย ###############################################                                                   
        ('PPE',                                 {'fields': ['equipment']}),

        ############################ ความเป็นอันตรายที่เกี่ยวข้องกับการทดลอง ############################################
        ('Hazards',                             {'fields': ['hazards']}),

        ########################################### การทิ้งของเสีย ##################################################
        ('Description of Warte Storage',        {'fields': ['w1', 'waste_group_w1',
                                                            'w2', 'waste_group_w2',
                                                            'w3', 'waste_group_w3',
                                                            'w4', 'waste_group_w4',
                                                            'w5', 'waste_group_w5',
                                                            'w6', 'waste_group_w6',
                                                            'w7', 'waste_group_w7',
                                                            'wx', 'waste_group_wx',
                                                            ]}),

        ########################################### ข้อแนะนำเพิ่มเติม ###############################################                                                  
        ('Suggestion',      {'fields': ['suggestion']}),
    ]
    list_display = ('id','course_number','course', 'degree', 'experiment_number', 'experiment_name')
    list_display_links = ('id', 'experiment_name')
    search_fields = ('course_number','course', 'experiment_number', 'experiment_name')
    list_filter = ['course','degree']

admin.site.register(Experiment,ExperimentAdmin)