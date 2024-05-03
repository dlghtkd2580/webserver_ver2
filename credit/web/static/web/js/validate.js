
function validate_form(page) {
       var re1 = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,10}$/;
       var re2 = /^[0-9]{1,4}$/;
       var re3 = /^[0-9]{1,3}$/;
       var re4 = /^[0-9]{1,9}$/;
       var re5 = /^[0-9]{1,2}$/;
       var re6 = /^[0-9]{1,4}$/;
       var re7 = /^[0-9]{1,9}$/;

       var re = /^[a-zA-Z0-9]{4,20}$/;
       var re = /^.{1,100}$/;
       var re = /^.{1,5000}$/;

       if(page=='form_2'){
           var name = document.getElementById("name");
           var age = document.getElementById("age");
           var phone_number_1 = document.getElementById("phone_number_1");
           var phone_number_2 = document.getElementById("phone_number_2");
           var phone_number_3 = document.getElementById("phone_number_3");
           var region = document.getElementById("region");

           if(!check(re1,name,"신청자 이름을 제대로 입력해주세요.")) {
               return false;
           }
           if(!check(re3,age,"나이를 제대로 입력해주세요.")) {
               return false;
           }
           if(!check(re2,phone_number_1,"전화번호 첫번쨰칸을 제대로 입력해주세요.")) {
               return false;
           }
           if(!check(re2,phone_number_2,"전화번호 두번째칸을 제대로 입력해주세요.")) {
               return false;
           }
           if(!check(re2,phone_number_3,"전화번호를 세번째칸을 입력해주세요.")) {
               return false;
           }

           document.getElementById('form_2').className += ' hidden';
           document.getElementById('form_3').className -=' hidden';
       }

       else if(page=='form_3'){

           var pay = document.getElementById("pay");
           var pay_day = document.getElementById("pay_day");

           if(!check(re4,pay,"월수입을 제대로 입력해주세요. 숫자만 입력가능합니다. (단위: 만원)")) {
               return false;
           }
           if(!check(re5,pay_day,"급여일을 제대로 입력해주세요. 1~31 까지의 숫자만 입력가능합니다.")) {
               return false;
           }

           document.getElementById('form_3').className += ' hidden';
           document.getElementById('form_4').className -=' hidden';
       }

       else if(page=='form_4'){
           var credit_grade = document.getElementById("credit_grade");

           if(!check(re6,credit_grade,"신용점수를 제대로 입력해주세요. 0~1000 까지의 숫자만 입력가능합니다.")) {
               return false;
           }

           document.getElementById('form_4').className += ' hidden';
           document.getElementById('form_5').className -=' hidden';
       }

       else if(page=='form_5'){
           document.getElementById('form_5').className += ' hidden';
           document.getElementById('form_6').className -=' hidden';
       }

       else if(page=='form_6'){
           var credit_amount = document.getElementById("credit_amount");

           if(!check(re7,credit_amount,"대출신청금액을 제대로 입력해주세요. 숫자만 입력가능합니다. (단위: 만원)")) {
               return false;
           }
       }
   }

function back_btn(){
    alert("심사 신청을 취소하고 처음으로 돌아갑니다.\n-모아중개-");
    location.href='http://127.0.0.1:8000/';
}


function validate_login() {

        var re1 = /^[a-zA-Z0-9]{1,20}$/;
        var re2 = /^.{1,20}$/;

        var user_id = document.getElementById("user_id");
        var user_pw = document.getElementById("user_pw");

        if(!check(re1, user_id, "아이디는 영문 또는 숫자 1~20자 이내 입니다.")) {
            return false;
        }

        if(!check(re2, user_pw, "비밀번호는 1~20자 이내 입니다.")) {
            return false;
        }

    }

  function validate_edit(){

    var re1 = /^[a-zA-Z0-9ㄱ-ㅎ|ㅏ-ㅣ|가-힣_]{1,20}$/;

    var file_new_name = document.getElementById("file_new_name");

    if(!check(re1, file_new_name, "글씨와 _(언더바)만 20자이내로 입력가능합니다.")) {
        return false;
    }

  }

function check(re, what, message) {
    if(re.test(what.value)) {
        return true;
    }
    alert(message);
    what.value = "";
    what.focus();
}
