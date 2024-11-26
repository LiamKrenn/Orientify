<script>
	export let degree = 0;
</script>

<div class="compass flex h-96 w-96 items-center justify-center">
	<p class="text-3xl">
		{degree.toFixed(1)}°
	</p>
	<div class="absolute" style="rotate: {degree - 90}deg">
		<div
			class="h-8 w-8 translate-x-[11.5rem] border-[1rem] border-transparent border-l-red-500"
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
