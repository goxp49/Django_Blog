KindEditor.ready(function (k) {
    window.editor = k.create('#id_article_content',{
        width: '800px',
        height: '400px',
        resizeType: 1,
        allowPreviewEmoticons: false,
        allowImageUpload: false,
        items: [
            'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
            'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
            'insertunorderedlist', '|', 'emoticons', 'link']
    });

    window.editor = k.create('#id_category_describe',{
        width: '800px',
        height: '400px',
        resizeType: 1,
        allowPreviewEmoticons: false,
        allowImageUpload: false,
        items: [
            'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
            'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
            'insertunorderedlist', '|', 'emoticons', 'link']
    });
});