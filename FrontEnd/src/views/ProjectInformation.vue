<template>
  <el-image :src="require('@/assets/group.jpg')" fit="contain"
  style="width: 50%; height: 15%"></el-image>
  <figure class='highcharts-figure'>
    <div id='container'></div>
    <p class="highcharts-description">
        <b>Motion Assessment Method Table</b>
    </p>
    <table id="datatable">
        <thead>
            <tr>
                <th>Abbreviation</th>
                <th>Terminology</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>BHG</th>
                <td>Breath-hold Gating</td>
                <td>Two methods to do BHG: actively and passively.
                    Active: The doctor could use the machine to
                    temporarily block the patient's breath.
                    Passive: Patients could actively hold their
                    breath (used in this survey)</td>
            </tr>
            <tr>
                <th>SABR</th>
                <td>Stereotactic Ablative Radiotherapy</td>
                <td>A highly focused radiation treatment that gives an
                    intense dose of radiation concentrated on a tumor,
                    while limiting the dose to the surrounding organs.</td>
            </tr>
            <tr>
                <th>Conventional</th>
                <td>Conventional Treatment</td>
                <td>The traditional way of treating cancer</td>
            </tr>
            <tr>
                <th>FBG</th>
                <td>Free-breathing Gating</td>
                <td>FBG is different from normal BHG and during the treatment of
                    FBG the patients are allowed to breathe normally while the MM
                    facilities try to capture the breadth pattern of the patient.</td>
            </tr>
            <tr>
                <th>TT</th>
                <td>Tumour Tracking</td>
                <td>The facility uses X-rays to first find the location of the tumor and
                    then computer algorithms are applied to the facilities to identify
                    the tumor at all times during the treatment. </td>
            </tr>
        </tbody>
    </table>
  </figure>
</template>

<script>
import Highcharts from 'highcharts';
// import accessibility from 'highcharts/modules/accessibility';

export default {
  methods: {
    displayHighCharts() {
      Highcharts.chart('container', {
        data: {
          table: 'datatable',
        },
      });
    },
  },
};
</script>
<style scoped>
.highcharts-data-table table {
  min-width: 310px;
  max-width: 800px;
  margin: 1em auto;
}

#datatable {
    font-family: Verdana, sans-serif;
    border-collapse: collapse;
    border: 1px solid #ebebeb;
    margin: 10px auto;
    text-align: center;
    width: 100%;
    max-width: 2000px;
}

#datatable caption {
    padding: 1em 0;
    font-size: 1.2em;
    color: #555;
}

#datatable th {
    font-weight: 600;
    padding: 0.5em;
}

#datatable td,
#datatable th,
#datatable caption {
    padding: 0.5em;
}

#datatable thead tr,
#datatable tr:nth-child(even) {
    background: #f8f8f8;
}

#datatable tr:hover {
    background: #f1f7ff;
}

</style>
