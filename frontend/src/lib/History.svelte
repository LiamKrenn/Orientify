<script>
	import { onMount } from 'svelte';
	import * as am5 from '@amcharts/amcharts5?client';
	import * as am5xy from '@amcharts/amcharts5/xy?client';
	import * as am5radar from '@amcharts/amcharts5/radar?client';
	import am5themes_Animated from '@amcharts/amcharts5/themes/Animated?client';

	export let history_data;
	export let steps = 10;

	const maxValue = Math.max(...Object.values(history_data));

	let chartdiv;

	onMount(() => {
		let root = am5.Root.new(chartdiv);
		root.setThemes([am5themes_Animated.new(root)]);

		let chart = root.container.children.push(
			am5radar.RadarChart.new(root, {
				panX: false,
				panY: false
			})
		);

		let xRenderer = am5radar.AxisRendererCircular.new(root, {});
		xRenderer.labels.template.setAll({ radius: 10, fill: am5.color('#fff') });
		xRenderer.grid.template.setAll({ stroke: am5.color('#fff'), strokeOpacity: 0.1 });

		let xAxis = chart.xAxes.push(
			am5xy.CategoryAxis.new(root, {
				maxDeviation: 0,
				categoryField: 'category',
				renderer: xRenderer,
				tooltip: am5.Tooltip.new(root, {})
			})
		);

		let yRenderer = am5radar.AxisRendererRadial.new(root, { minGridDistance: 20 });
		yRenderer.labels.template.setAll({ forceHidden: true }); // Hide y-axis labels
		yRenderer.grid.template.setAll({ stroke: am5.color('#fff'), strokeOpacity: 0.1 });

		let yAxis = chart.yAxes.push(
			am5xy.ValueAxis.new(root, {
				min: 0,
				renderer: yRenderer
			})
		);

		let data = [];
		for (let i = 0; i < 360; i += steps) {
			data.push({
				category: `${i}-${i + steps}°`,
				value: history_data[`${i}-${i + steps - 1}`] || 0
			});
		}

		function interpolateColor(value, min, max) {
			const startColor = { r: 0, g: 123, b: 255 }; // Blue
			const endColor = { r: 255, g: 165, b: 0 }; // Orange

			const ratio = (value - min) / (max - min);
			const r = Math.round(startColor.r + ratio * (endColor.r - startColor.r));
			const g = Math.round(startColor.g + ratio * (endColor.g - startColor.g));
			const b = Math.round(startColor.b + ratio * (endColor.b - startColor.b));

			return am5.color(`rgb(${r},${g},${b})`);
		}

		let series = chart.series.push(
			am5radar.RadarColumnSeries.new(root, {
				xAxis: xAxis,
				yAxis: yAxis,
				valueYField: 'value',
				categoryXField: 'category'
			})
		);

		series.columns.template.setAll({
			tooltipText: '{categoryX}: {valueY}',
			strokeOpacity: 0,
			width: am5.p100
		});

		series.columns.template.adapters.add('fill', (fill, target) => {
			let value = target.dataItem.get('valueY');
			return interpolateColor(value, 0, maxValue);
		});

		series.data.setAll(data);
		xAxis.data.setAll(data);

		// Animate chart
		series.appear(1000);
		chart.appear(1000, 100);
	});
</script>

<div id="chartdiv" bind:this={chartdiv}></div>

<style>
	#chartdiv {
		width: 100%;
		height: 600px;
	}
</style>
