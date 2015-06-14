$(function() {
	carregaDatepicker();
	carregaTab();
  carregaSelect2();
});

function carregaDatepicker(){
    //cria o datepicker com op��o de mes e ano
	$( ".datepicker" ).datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "c-100:c"
      }, $.datepicker.regional[ "pt-BR" ]);

	//retira a edicao do campo
	$('.datepicker').attr('editable', false);
  }

function carregaTab(){
	$( ".tabs" ).tabs().addClass( "ui-tabs-vertical ui-helper-clearfix" );
    $( ".tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );
}

//Configura o componente chosen
function carregaSelect2(){
  $(".select2").select2();
}