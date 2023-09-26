from itemadapter import ItemAdapter


class SpaceflightPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == 'rocket_name':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace('\n', '').strip()
            if field_name == 'rocket_status':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace('Status:', '').strip()
            if field_name == 'price':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace('Price:', '').strip()

        return item
