export function logout() {
    localStorage.removeItem("login");
    localStorage.removeItem("password");
    localStorage.removeItem("is_admin");
}

export function isLoggedIn() {
    if(localStorage.getItem("login")){
        return true;
    }else{
        return false;
    }
}

export function isAdmin() {
    if(localStorage.getItem("is_admin") == 'true'){
        return true;
    }else{
        return false;
    }
}

