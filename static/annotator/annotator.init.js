jQuery(function ($) {
    var content = $('#annotateit').annotator();
    content.annotator('addPlugin', 'Tags');
    content.annotator('addPlugin', 'Filter');
    content.annotator('addPlugin', 'Store', {
        prefix:''
    });
});