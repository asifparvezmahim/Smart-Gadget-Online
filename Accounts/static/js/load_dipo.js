$(document).ready(function(){
    $("#loadMore").on('click',function(){
        var _currentDepoHistory = $(".dipo-box").length; 
        var _limit = $(this).attr("data-limit");
        var _total = $(this).attr("total-data");
        

        // start ajax
          $.ajax({
            url:'/load-more-deposit',
            data:{
                limit : _limit,
                offset:_currentDepoHistory
            },
            dataType:'json',
            beforeSend:function(){
             $("#loadMore").attr('disabled',true);
             $(".load-more-icon").addClass('fa-spin');

            },
            success:function(res){
                $("#loadMore").attr('disabled',false);
                $(".load-more-icon").removeClass('fa-spin'); 
            }
          });
        //end
    })
})