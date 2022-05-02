import {
  createRouter,
  createWebHistory
} from 'vue-router'
import Home from '../views/Home.vue'
import HacroMap from '../views/HacroMap.vue'
import HealthRelatedTopicTrend from '../views/HealthRelatedTopicTrend.vue'
import SymptomTimelineAnalysis from '../views/SymptomTimelineAnalysis.vue'

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Hacromap',
    name: 'HacroMap',
    component: HacroMap
  },
  {
    path: '/healthrelatedtopictrend',
    name: 'Health Related Topic Trend',
    component: HealthRelatedTopicTrend
  },
  {
    path: '/symptomtimelineanalysis',
    name: 'Symptom Timeline Analysis',
    component: SymptomTimelineAnalysis,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
