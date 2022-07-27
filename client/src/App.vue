<template>
  <div id="app">
    <b-container>
      <b-row class="text-center" align-h="center">
        <img alt="jcbachmann logo" src="./assets/logo.png">
      </b-row>
      <b-row class="text-center pt-4" align-h="center">
        <b-card class="ma-2 pa-2 h-100 w-75">
          <b-card-title>{{title}}</b-card-title>
          <Plotly v-if="data.length" :data="data" :layout="layout" :display-mode-bar="true" class="mb-3"></Plotly>
          <b-button :disabled="data.length > 0" @click="loadContent()" variant="primary">Load Chart</b-button>
        </b-card>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { Plotly } from 'vue-plotly'

export default {
  name: 'App',
  components: {
    Plotly
  },
  data() {
    return {
      title: "This is the demo for JCB",
      data:[],
      layout:{
        showLegend: false,
        title: "1000 random numbers and its modules 10",
        xaxis: {
          title: {
            text: 'Randon Number',
            font: {
              size: 18,
            }
          },
        },
        yaxis: {
          title: {
            text: 'Module 10',
            font: {
              size: 18,
            }
          }
        }
      },
    }
  },
  methods: {
    onContext(ctx) {
      this.context = ctx
    },
    async loadContent(){
      await fetch('/data')
        .then(response => response.json())
        .then(({a, b}) => {
          this.data.push({
            x: a,
            y: b,
            type: 'scatter', mode: 'markers',
          })
        });
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
