<script lang="ts">
	import { PUBLIC_DB_IP, PUBLIC_DB_PORT } from '$env/static/public';
	import History from '$lib/History.svelte';
	import { onMount } from 'svelte';

	const steps = 10;
	let history_data: { [range: string]: number } = {};

	onMount(async () => {
		let res = await fetch(
			`http://${PUBLIC_DB_IP}:${PUBLIC_DB_PORT}/orientation/grouped/?steps=` + steps
		);
		history_data = await res.json();
	});
</script>

{#if Object.keys(history_data).length > 0}
	<History {history_data} {steps} />
{/if}
