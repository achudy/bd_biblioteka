import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import ReaderProfile from "../views/ReaderProfile.vue";
import Page404 from "../views/404.vue";
import Registration from "../views/Registration.vue";
import EmployeeProfile from "../views/EmployeeProfile.vue";

import {isLoggedIn, isAdmin} from "../utils/auth.js";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      allowAnonymous: true
    }
  },

  {
    path: "/books",
    name: "Books",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Books.vue"),
    meta: {
        allowAnonymous: true
      }
  },
  {
    path: "/Registration",
    name: "Registration",
    component: Registration,
    meta: {
      allowAnonymous: true
    }
  },

  {
    path: "/ReaderProfile",
    name: "ReaderProfile",
    component: ReaderProfile,
    meta: {
      allowAnonymous: false
    }
  },
  
  {
    path: "/EmployeeProfile",
    name: "EmployeeProfile",
    component: EmployeeProfile,
    meta: {
      allowAnonymous: false,
      allowReaders: false
    }
  },
    
  {
    path: "/*",
    name: "Page404",
    component: Page404,
    meta: {
      allowAnonymous: true
    }
  },

];

const router = new VueRouter({
  mode: "hash",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  
  if(to.name == "Registration" && isLoggedIn() && !isAdmin()){
    next({
      path: '/ReaderProfile',
      query: { redirect: to.fullPath }
    })
  }else if(to.name == "Registration" && isLoggedIn() && isAdmin()){
    next({
      path: '/EmployeeProfile',
      query: { redirect: to.fullPath }
    })
  }else

  if (!to.meta.allowAnonymous && !isLoggedIn()) {
    next({
      path: '/Registration',
      query: { redirect: to.fullPath }
    })
  }
  else {
    next()
  }  
})

export default router;
