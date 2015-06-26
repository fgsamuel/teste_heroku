$("#formAjax").submit(function() {

  ids = $(this).attr('atualizarIds');

    $.ajax({
           type: $(this).attr('method'),
           url: $(this).attr('action'),
           data: $(this).serialize(), // serializes the form's elements.
           success: function(data)
           {
           		//se for zero, é sucesso, e manda um objeto com id e nome
           		 if(data['return'] == 0){
           		 	//retiro o modal da tela
           		 	$('#myModal').modal('hide');

           		 	//monto uma string com a opção
           		 	var option = '<option value="' + data['obj']['id'] + '">' + data['obj']['nome'] + '</option>'
           		 	//adiciono a opção no select
           		 	$(ids).append(option)
           		 	
           		 }else{
           		 	$('#divForm').html(data['html'])
           		 }
           		 
           },
           error : function(data){
           	alert('erro')
           }
         });

    return false; // avoid to execute the actual submit of the form.
});

function ajax(obj){
	url = $(obj).attr('url');
	ids = $(obj).attr('atualizarIds');
	divId = $(obj).attr('divId');
	modalId = $(obj).attr('modalId')

  $('#formAjax').attr('action', url);
  $('#formAjax').attr('atualizarIds', ids);
	
	$('#verbose').html($(obj).text())
	$().html($(obj).text())
	
	$.get(url, function(data, status){
       $(divId).html(data)
       $(modalId).modal('show');
    });
}