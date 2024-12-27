<script lang="ts">
	import '@fortawesome/fontawesome-free/css/all.min.css';
	import '../app.css';
	export const prerender = true;
	let { children } = $props();
</script>

<nav>
	<div class="nav-content">
		<div class="logo">
			<a href="/">Hai Dang</a>
		</div>
	</div>
</nav>

<main>
	{@render children()}
</main>

<footer>
	<p>© {new Date().getFullYear()} Hai Dang. All rights reserved.</p>
</footer>

<style>
	nav {
		background: #ffffff;
		box-shadow: 0 2px 4px rgba(0,0,0,0.1);
		position: fixed;
		width: 100%;
		top: 0;
		z-index: 1000;
	}

	.nav-content {
		max-width: 1200px;
		margin: 0 auto;
		padding: 1rem 2rem;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.logo a {
		font-size: 1.5rem;
		font-weight: bold;
		text-decoration: none;
		color: #333;
	}

	.nav-links a {
		margin-left: 2rem;
		text-decoration: none;
		color: #666;
		transition: color 0.3s ease;
	}

	.nav-links a:hover {
		color: #000;
	}

	main {
		max-width: 1200px;
		margin: 80px auto 0;
		padding: 2rem;
		min-height: calc(100vh - 160px);
	}

	footer {
		text-align: center;
		padding: 2rem;
		background: #f5f5f5;
	}

	@media (max-width: 768px) {
		.nav-content {
			flex-direction: column;
			padding: 1rem;
		}

		.nav-links {
			margin-top: 1rem;
		}

		.nav-links a {
			margin: 0 0.5rem;
			font-size: 0.9rem;
		}
	}
</style>
