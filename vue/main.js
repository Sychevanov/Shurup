
new Vue({
  el: '#button',
  data:{
    loginYes:'',
    login:'',
    pass:''
  },
  methods: {
    logPass: function (login,pass) {
      if (this.login=='test' && this.pass=='test' ){
        
        this.loginYes='вы залогинились'
      }
      else
      this.loginYes='введите правильный логин и пароль'
      
      }
    }
  
});