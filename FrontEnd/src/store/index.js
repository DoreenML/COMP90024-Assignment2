import { createStore } from 'vuex';

export default createStore({
  state: {
    buttonArray: [{
      key: 'ITV',
      text: 'ITV',
      type: 'primary',
    }, {
      key: 'BHG',
      text: 'BHG',
      type: 'success',
    }, {
      key: 'FBG',
      text: 'FBG',
      type: 'info',
    }],
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
});
