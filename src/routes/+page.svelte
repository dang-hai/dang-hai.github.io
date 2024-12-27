<script lang="ts">
  import { newsItems } from '$lib/data/news';
  import { featuredResearch } from '$lib/data/research';
  
  let visibleItems = 5;
  
  function loadMore() {
    visibleItems += 5;
  }
</script>

<main class="container mx-auto px-4 py-8">
  <section class="hero mb-12">
    <!-- Profile Section -->
    <div class="flex flex-col md:flex-row items-center md:items-start gap-8 mb-8">
      <!-- Profile Image -->
      <img 
        src="/profile.jpeg" 
        alt="Hai Dang" 
        class="w-48 h-48 rounded-full object-cover shadow-lg"
      />
      
      <!-- Text Content -->
      <div>
        <h1 class="text-4xl font-bold mb-4">Hello, I'm Hai 👋</h1>
        
        <!-- Location indicator -->
        <div class="flex items-center gap-2 text-gray-700 mb-6">
          <i class="fas fa-location-dot"></i>
          <span>Munich 🇩🇪 & San Francisco 🇺🇸</span>
        </div>
        
        <!-- Social Links -->
        <div class="flex gap-6 mb-8">
          <a href="/#contact" 
             class="text-gray-700 hover:text-primary transition-colors"
             aria-label="Email">
            <i class="fas fa-envelope text-2xl"></i>
          </a>
          <a href="https://scholar.google.com/citations?user=-BpP7hsAAAAJ&hl" 
             target="_blank" 
             rel="noopener" 
             class="text-gray-700 hover:text-primary transition-colors"
             aria-label="Google Scholar">
            <i class="fas fa-graduation-cap text-2xl"></i>
          </a>
          <a href="https://github.com/dang-hai" 
             target="_blank" 
             rel="noopener" 
             class="text-gray-700 hover:text-primary transition-colors"
             aria-label="GitHub">
            <i class="fab fa-github text-2xl"></i>
          </a>
          <a href="https://www.linkedin.com/in/hdng/" 
             target="_blank" 
             rel="noopener" 
             class="text-gray-700 hover:text-primary transition-colors"
             aria-label="LinkedIn">
            <i class="fab fa-linkedin text-2xl"></i>
          </a>
        </div>

        <p class="text-xl text-gray-700 mb-6">
            I build systems that help people work better with AI, drawing on my background in human-computer interaction (HCI) and machine learning (ML).
        </p>
        <p class="text-xl text-gray-700 mb-6">
            I completed my PhD in HCI at the <a href="https://www.hciai.uni-bayreuth.de/en/index.html" class="text-blue-600 hover:text-blue-800 underline" target="_blank" rel="noopener">University of Bayreuth's HCI+AI Lab</a>, working with Prof. Dr. Daniel Buschek. Prior to that, I received my B.Sc. and M.Sc. in Computer Science from <a href="https://www.lmu.de/en/" class="text-blue-600 hover:text-blue-800 underline" target="_blank" rel="noopener">LMU Munich</a> . My research experience includes work at <a href="https://about.meta.com/realitylabs/" class="text-blue-600 hover:text-blue-800 underline" target="_blank" rel="noopener">Meta Reality Labs Research</a>, <a href="https://www.research.autodesk.com" class="text-blue-600 hover:text-blue-800 underline" target="_blank" rel="noopener">Autodesk Research</a>, and the <a href="https://glassmanlab.seas.harvard.edu" class="text-blue-600 hover:text-blue-800 underline" target="_blank" rel="noopener">Harvard Variation Lab</a> with Prof. Elena Glassman.
        </p>
        <p class="text-xl text-gray-700 mb-6">
            I've recently co-founded a startup building advanced AI systems to understand complex construction documents. Our focus is on building intuitive human-AI workflows that augment industry experts, starting with intelligent quote processing. 
        </p>

        <!-- Research Interests -->
        <div class="mb-8">
            <h2 class="text-xl font-semibold mb-3">Research Interests</h2>
            <div class="flex flex-wrap gap-2">
                <span class="px-4 py-2 bg-blue-50 text-blue-700 rounded-lg">Interactive NLP</span>
                <span class="px-4 py-2 bg-blue-50 text-blue-700 rounded-lg">Human-AI Collaboration</span>
                <span class="px-4 py-2 bg-blue-50 text-blue-700 rounded-lg">Creative Support Tools</span>
                <span class="px-4 py-2 bg-blue-50 text-blue-700 rounded-lg">Human-Centered AI System Design</span>
            </div>
        </div>

        <!-- Interest Callout -->
        <div class="bg-blue-50 border-l-4 border-blue-500 p-4 mb-8 rounded-r">
          <div class="flex items-start">
            <div class="flex-shrink-0">
              <i class="fas fa-lightbulb text-blue-500 text-xl mt-1"></i>
            </div>
            <div class="ml-3">
              <p class="text-blue-600">
                If you're passionate about interactive AI and transforming how construction professionals work, let's chat about building intelligent tools together.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="news mb-12">
    <h2 class="text-2xl font-semibold mb-6">News</h2>
    <div class="space-y-8">
      {#each newsItems.slice(0, visibleItems) as item}
        <div class="news-item flex gap-6 items-start">
          <img 
            src={item.image.src} 
            alt={item.image.alt} 
            class="w-32 h-32 object-cover rounded-lg flex-shrink-0"
          />
          <div class="flex-1 max-w-2xl">
            <div class="text-sm text-gray-600 mb-2">[{item.date}]</div>
            <p class="text-gray-700">
              {@html item.content}
            </p>
          </div>
        </div>
      {/each}
    </div>
    
    {#if visibleItems < newsItems.length}
      <div class="text-center mt-8">
        <button
          on:click={loadMore}
          class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
        >
          Load More
        </button>
      </div>
    {/if}
  </section>

  <section class="expertise mb-12">
    <h2 class="text-2xl font-semibold mb-6">Featured Research</h2>
    <div class="grid grid-cols-1 gap-8">
        {#each featuredResearch as research}
            <div class="project-card p-6 bg-gray-50 rounded-lg">
                <h3 class="text-xl font-medium mb-3">{research.title}</h3>
                <p class="text-gray-700 mb-4">
                    {research.description}
                </p>
                <div class="flex flex-wrap gap-2 mb-4">
                    {#each research.tags as tag}
                        <span class="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">{tag}</span>
                    {/each}
                </div>
                <div class="text-sm text-gray-600 flex flex-col gap-2">
                    {#each research.publications as pub}
                        <a href={pub.url} class="text-blue-600 hover:text-blue-800 hover:underline" target="_blank" rel="noopener">
                            {pub.title}
                            <span class="text-gray-600 block mt-1">{pub.venue}</span>
                        </a>
                    {/each}
                </div>
            </div>
        {/each}
    </div>
  </section>
</main>

<style>
  .container {
    max-width: 1200px;
  }
  
  .skill-card {
    transition: transform 0.2s;
  }
  
  .skill-card:hover {
    transform: translateY(-2px);
  }
  
  /* If you want to customize the hover color, define your primary color */
  :root {
    --color-primary: #0066cc; /* or your preferred color */
  }
  
  .hover\:text-primary:hover {
    color: var(--color-primary);
  }
</style>
