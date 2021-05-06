import { InjectionKey } from "vue";
import { createStore, Store, useStore as baseUseStore } from "vuex";
import { Tweet } from "../types/task";
import axios from "axios";

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
    setTweet(state: GlobalState, payload: Tweet[]) {
      state.tweets.push(...payload);
    },
    addTweet(state: GlobalState, payload: Tweet) {
      state.tweets.unshift(payload);
    },
    removeTweet(state: GlobalState, id: string) {
      state.tweets = state.tweets.filter((t) => t.id !== id);
    },
  },
  actions: {
    async listTweet({ commit }) {
      const { data } = await axios.get("http://localhost:8000/api/v1/twitter/");
      commit("setTweet", data);
    },
    async postTweet({ commit }, payload) {
      const { data } = await axios.post(
        "http://localhost:8000/api/v1/twitter/",
        payload
      );
      commit("addTweet", data);
    },
    async updateTweet({ commit }, payload) {
      const { data } = await axios.put(
        `http://localhost:8000/api/v1/twitter/${payload.id}`,
        payload
      );
    },
    async deleteTweet({ commit }, id) {
      await axios.delete(`http://localhost:8000/api/v1/twitter/${id}`);
      commit("removeTweet", id);
    },
  },
});

// useState を呼び出す度、 StateKey で型を定義するのを避けるために、ここであらかじめ定義する
export function useStore() {
  return baseUseStore(StateKey);
}
