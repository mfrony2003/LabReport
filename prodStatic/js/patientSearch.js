var diagonysisData = [];
    var totalPrice = [];

    

    function clearItem()

    {

        $('#tblDiagonysis').html('');
        $('#spnTotal').html('');
    }

    function addItem() {

        var element = $("#ddldiagonisis option:selected");
        name = element.text();
        price = element.attr('price');
        id = element.val();

        // add:
        diagonysisData.push(id);
        totalPrice.push(price)

        let dynamicRowHTML = `
            <tr id=${id}> 
                <td > 
                     ${id}
                </td>
                <td > 
                     ${name}
                </td> 
                <td > 
                     ${price}
                </td>
                             
            </tr>`;
        $('#tblDiagonysis').append(dynamicRowHTML);
        sum = 0
        for (var i = 0; i < totalPrice.length; i++) {
            sum += totalPrice[i] << 0;
        }

        $('#spnTotal').html(sum);


    }

    $('.likebutton').click(function () {

        var _patientId = $('input[id=hdnpatientId]').val();
    
        $.ajax({
            type: "POST",
            url: $(this).data('url'),
    
            data: {
                list: JSON.stringify(diagonysisData),
                patientId:_patientId,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {                
               
                
                window.location.href='/patientReportList/'+data.ReportId
            },
            complete: function (data) {     
                
                
        }
    });
    })
    

    


    $('#diagonisisAddModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        console.log(button)
        var patientId = button.data('patientid') // Extract info from data-* attributes
        var patientName = button.data('patientName') // Extract info from data-* attributes       
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this)
        modal.find('.card-title').text('Diagonisis ')
        modal.find('#hdnpatientId').val(patientId)
        //   modal.find('.modal-body input').val(recipient)
    })