from SpiderProject.entity.Job import Job
from SpiderProject.entity.Job import SESSION
from datetime import datetime
from collections import Counter


class JobDao(object):
    def __init__(self):
        self.mysql_session = SESSION()

    def insert(self, item):
        crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = Job(
            job_sn=item['positionId'],
            job_name=item['positionName'],
            company_abbreviation=item['companyShortName'],
            work_year=item['workYear'],
            education=item['education'],
            company_name=item['companyFullName'],
            city=item['city'],
            company_id=item['companyId'],
            company_bussiness=item['industryField'],
            company_bonus=','.join(item['companyLabelList']),
            wealthy=item['salary'],
            type=item['jobNature'],
            company_type=item['financeStage'],
            company_size=item['companySize'],
            job_tags=item['positionAdvantage'],
            create_time=datetime.strptime(item['createTime'], '%Y-%m-%d %H:%M:%S'),
            crawl_time=crawl_time,
            longitude=item['longitude'],
            latitude=item['latitude']
        )
        query_result = self.mysql_session.query(Job).filter(Job.crawl_time == crawl_time,
                                                            Job.job_sn == item['positionId']).first()
        if query_result:
            pass
        else:
            self.mysql_session.add(data)
            self.mysql_session.commit()

    def query_indestury_field(self):
        info = {}
        result = self.mysql_session.query(Job.company_bussiness).filter(
            Job.crawl_time.notilike(datetime.now().strftime('%Y-%m-%d'))
        ).all()
        result_list = [x[0].split(',')[0] for x in result]
        count_list = [x for x in Counter(result_list).items() if x[1] > 10]
        data = [{'name': x[0], 'value': x[1]} for x in count_list]
        name_data = [name['name'] for name in data]
        info['labels'] = name_data
        info['data'] = data
        return info


# if __name__ == '__main__':
#     test = JobDao()
#     test.query_indestury_field()
