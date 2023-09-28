from itemadapter import ItemAdapter
from datetime import datetime


class SpaceflightPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()

        date_format = '%a %b %d, %Y %H:%M %Z'

        for field_name in field_names:
            if field_name == 'date':
                value = adapter.get(field_name)
                adapter[field_name] = datetime.strptime(value, date_format)
            if field_name == 'rocket_name':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace('\n', '').strip()
            if field_name == 'rocket_status':
                value = adapter.get(field_name)
                if 'Status:' in value:
                    adapter[field_name] = value.replace('Status:', '').strip()
                else:
                    adapter[field_name] = None
            if field_name == 'price':
                value = adapter.get(field_name)
                if 'Price:' in value:
                    adapter[field_name] = value.replace('Price: $', '').replace("million", "").strip()
                else:
                    adapter[field_name] = None

        return item
