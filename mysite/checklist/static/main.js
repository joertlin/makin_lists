$( document ).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');

    var checklists = $('#checklists');
    var checklist_name = $('#checklist_name')
    
    function append_new_checklist(data){
        if (data.list_name != '') {
            checklists.append('<button type="button" class="list-group-item">' + data.list_name + '</button>')
            //checklists.append('<li><a href="' + data.pk + '/">' + data.list_name + '</a></li>');
        }
    };

        
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var indexPath = document.getElementById("indexPath").value;

    $('#add_checklist').on('click', function(){
        if (checklist_name.val() != '') {
            $.ajax({
                type: 'POST',
                url: indexPath + 'add_checklist' + "/",
                data: {checklist_name: checklist_name.val()},
                success: function(gotoList) {
                    //gotoList = JSON.parse(gotoList);
                    //url = indexPath + gotoList.pk + "/";
                    //$( location ).attr("href", url);
                    newChecklist = JSON.parse(gotoList);
                    append_new_checklist(newChecklist);
                    //alert('new entry:' + newChecklist.list_name);
                },
                error: function() {
                    alert('error posting new list name!')
                }
            });
        }
    });
});
