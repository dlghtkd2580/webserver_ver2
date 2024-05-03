$(document).ready(function(){
  $('.logout_btn').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','#494db3');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','#1e2d3b');
    $(this).css('background','white');
  });
  $('.form_delete_btn').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','red');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','#1e2d3b');
  });
  $('.form_delete_all_btn').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','red');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','#1e2d3b');
  });
  $('.file_delete_btn > button').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','red');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','#1e2d3b');
  });
  $('.file_delete_all_btn').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','red');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','#1e2d3b');
  });
  $('.file_edit_btn > button').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','red');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).css('background','#1e2d3b');
  });
});

function delete_all_check(message) {
        if (!confirm(message + "DB가 전부 삭제 됩니다.\n정말로 전부 삭제 하시겠습니까?")) {
            return false;
        } else {
          alert(message + "DB가 전부 삭제 되었습니다.");
          return true;
        }
}
