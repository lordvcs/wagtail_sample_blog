from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname='full title')
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/column.html'

class TwoColumnBlock(blocks.StructBlock):
    left_column = ColumnBlock(icon='left-arrow', label='Left column content')
    right_column = ColumnBlock(icon='right-arrow', label='Right column content')

    class Meta:
        template = 'blog/blocks/two_colum_block.html'