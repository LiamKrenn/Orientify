<script>
	export let degree = 0;
	export let size = 1;
</script>

<div
	class="compass flex items-center justify-center bg-slate-800"
	style="height: {24 * size}rem; width: {24 * size}rem"
>
	<p style="font-size: {1.875 * size}rem; line-height: {2.25 * size}rem">
		{degree.toFixed(1)}°
	</p>
	<div class="absolute duration-150" style="rotate: {degree - 90}deg">
		<div
			style="height: {2 * size}rem; width: {2 * size}rem; transform: translate({11.45 *
				size}rem, 0); border-width: {size}rem;"
			class="border-transparent border-l-red-500"
		></div>
	</div>
</div>

<style>
	.compass {
		background: radial-gradient(
				circle,
				#0f172a 0%,
				#0f172a 62%,
				transparent 62%,
				transparent 70%,
				#0f172a 70%
			),
			repeating-conic-gradient(#334155 -0.4deg 0.4deg, transparent 0.4deg 89.6deg),
			repeating-conic-gradient(#1e293b -0.25deg 0.25deg, transparent 0.25deg 4.75deg);
	}
</style>
