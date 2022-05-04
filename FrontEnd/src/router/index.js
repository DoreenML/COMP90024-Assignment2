import {
  createRouter,
  createWebHistory
} from 'vue-router'
import Home from '../views/Home.vue'
import HacroMap from '../views/HacroMap.vue'
import HealthRelatedTopicTrend from '../views/HealthRelatedTopicTrend.vue'
import SymptomTimelineAnalysis from '../views/SymptomTimelineAnalysis.vue'
import DepressionAnalysis from '../views/DepressionAnalysis.vue'
import AgeDistribution from '../views/AgeDistribution.vue'
import GenderAnalysis from '../views/GenderAnalysis.vue'
import ViolentTweet from '../views/ViolentTweet.vue'
import CrimeHeatMap from '../views/CrimeHeatMap.vue'
import ProjectInformation from '../views/ProjectInformation.vue'
import TeamInformation from '../views/TeamInformation.vue'

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
  },
  {
    path: '/depressionanalysis',
    name: 'Depression Analysis',
    component: DepressionAnalysis,
  },
  {
    path: '/agedistribution',
    name: 'Age Distribution',
    component: AgeDistribution,
  },
  {
    path: '/genderanalysis',
    name: 'Gender Analysis',
    component: GenderAnalysis,
  },
  {
    path: '/violentweet',
    name: 'Violent Tweet',
    component: ViolentTweet,
  },
  {
    path: '/crimeheatmap',
    name: 'Crime Heat Map',
    component: CrimeHeatMap,
  },
  {
    path: '/projectinformation',
    name: 'Project Information',
    component: ProjectInformation,
  },
  {
    path: '/teaminformation',
    name: 'Team Information',
    component: TeamInformation,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
