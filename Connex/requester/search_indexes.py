from haystack import indexes
from .models import Challenge

class MobileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    category =indexes.CharField(model_attr='category')
    story = indexes.CharField(model_attr='story')

    title_auto = indexes.EdgeNgramField(model_attr='title')
    category_auto = indexes.EdgeNgramField(model_attr='category')
    story_auto = indexes.EdgeNgramField(model_attr='story')
    suggestions = indexes.FacetCharField()

    def get_model(self):

        return Challenge

    def index_queryset(self, using=None):
        “””Used when the entire index for model is updated.”””
        return self.get_model().objects.all()

    def prepare(self, obj):
        prepared_data = super(MobileIndex, self).prepare(obj)
        prepared_data['suggestions'] = prepared_data['text'] return prepared_data