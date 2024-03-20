 
    $('.likebutton').click(function () {

        var _reportId = $(this).attr('data-reportid');
        var _diagnosisid = $(this).attr('data-diagnosis');
        var _specimenid = $(this).attr('data-specimen');
        
        $(this).hide()
        $(this).next().show()
        
        saveSpecimenData = { 'reportId': _reportId,
                            'diagnosisid' :_diagnosisid,
                            'specimenid': _specimenid
                        }
                        
        
        $.ajax({
            type: "POST",
            url: $(this).data('url'), 
        
            data: {        
                saveSpecimenData: JSON.stringify(saveSpecimenData),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {                
                
                
                
            },
            complete: function (data) {     
                
                
        }
        });
        })