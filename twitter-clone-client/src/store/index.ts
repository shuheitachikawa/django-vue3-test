import { InjectionKey } from "vue";
import { createStore, Store, useStore as baseUseStore } from "vuex";
import { Tweet } from "../types/task";

export interface GlobalState {
  count: number;
  tweets: Tweet[];
}
export const StateKey: InjectionKey<Store<GlobalState>> = Symbol();

export const store = createStore({
  state() {
    return {
      count: 0,
      tweets: [],
    };
  },
  getters: {
    count(state: GlobalState) {
      return state.count;
    },
    tweets(state: GlobalState) {
      return state.tweets;
    },
  },
  mutations: {
    increment(state: GlobalState) {
      state.count++;
    },
    addTweet(state: GlobalState, payload: Tweet) {
      state.tweets.unshift(payload);
    },
  },
});

// useState を呼び出す度、 StateKey で型を定義するのを避けるために、ここであらかじめ定義する
export function useStore() {
  return baseUseStore(StateKey);
}
